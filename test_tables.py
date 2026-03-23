import sys
import os
from unstructured.partition.pdf import partition_pdf

def main():
    # 1. 명령행 인자 체크
    if len(sys.argv) < 2:
        print("사용법: python test_tables.py <pdf_file_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print(f"에러: 파일을 찾을 수 없습니다 -> {pdf_path}")
        sys.exit(1)

    # 이미지 저장 폴더 생성
    output_dir = "extracted_assets"
    os.makedirs(output_dir, exist_ok=True)

    print(f"[{pdf_path}] 분석 중... 잠시만 기다려주세요.")

    # 2. Unstructured 파싱 실행
    elements = partition_pdf(
        filename=pdf_path,
        strategy="hi_res",           # 표와 그림을 찾으려면 고해상도 전략 필수
        infer_table_structure=True,  # 표 구조 인식 엔진 가동
        extract_images_in_pdf=True,  # 그림/그래프 파일로 저장
        extract_image_block_output_dir="extracted_assets",
    
        # [핵심] 텍스트가 이미 있는 디지털 PDF라면 Tesseract(OCR) 대신 
        # 내장 텍스트 추출기(pdfminer)를 우선 사용하도록 유도합니다.
        pdf_infer_table_structure=True, 
        languages=["kor", "eng"],
    
        # 필요하다면 아래 옵션으로 OCR이 텍스트를 건드리지 못하게 조절 가능합니다.
        # ocr_languages="kor+eng", 
    )

    print(f"\n검출된 전체 요소 수: {len(elements)}")

    # 3. 결과 분류 및 출력
    tables = [el for el in elements if el.category == "Table"]
    images = [el for el in elements if el.category == "Image"]
    
    print(f"검출된 표(Table) 수: {len(tables)}")
    print(f"검출된 그림(Image/Figure) 수: {len(images)}")

    # 표 상세 처리
    for i, table in enumerate(tables, start=1):
        print("\n" + "=" * 80)
        print(f"[Table {i}]")
        print(f"Page: {getattr(table.metadata, 'page_number', 'N/A')}")

        # HTML 구조 저장 (LLM 전달용으로 가장 좋음)
        html = getattr(table.metadata, "text_as_html", None)
        if html:
            html_name = f"table_{i}.html"
            with open(os.path.join(output_dir, html_name), "w", encoding="utf-8") as f:
                f.write(html)
            print(f"-> HTML 표 저장 완료: {html_name}")

        # 텍스트 프리뷰 (너무 길면 자름)
        print(f"Preview: {(table.text or '')[:200]}...")

    # 전체 흐름 확인 (Table 주변 맥락)
    print("\n\n" + "### 문서 구조 흐름 (Table 중심) ###")
    for idx, el in enumerate(elements):
        if el.category == "Table":
            print("-" * 50)
            # 앞뒤 2개씩만 출력하여 맥락 확인
            start = max(0, idx - 2)
            end = min(len(elements), idx + 3)
            for j in range(start, end):
                marker = ">>>" if j == idx else "   "
                print(f"{marker} [{j}] {elements[j].category}: {elements[j].text[:100]}...")

if __name__ == "__main__":
    main()