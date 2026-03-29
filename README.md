# 📑 정부 보고서 데이터 구조화 프로젝트 (졸업 프로젝트)

본 프로젝트는 500페이지 내외의 방대한 정부 및 지자체 보고서(PDF)에서 핵심 정량 데이터(표, 수치)를 AI 모델을 통해 자동으로 추출하고, 이를 LLM 분석이 용이한 구조화된 데이터(Markdown/CSV)로 변환하는 시스템을 구축하는 것을 목표로 합니다.

---

## 🚀 프로젝트 진행 현황

### 1. 완료된 작업 (Milestones)
* **환경 구축**: macOS(Apple Silicon) 및 Windows 환경에서 Python 가상환경 및 AI 의존성 설정 완료.
* **전처리 도구 선정**: `Unstructured` 대비 한국어 표 인식률 및 처리 속도가 뛰어난 **Marker-pdf** 엔진 도입.
* **대규모 데이터 변환**: 약 500페이지 분량의 `seoul_re100.pdf`를 마크다운(`seoul_re100.md`)으로 변환 성공.
    * 변환 소요 시간: 약 3.8시간 (CPU 연산 기준)
    * 성과: 복잡한 표 구조를 `|---|` 형태의 마크다운 포맷으로 유지하며 텍스트 손실 최소화.

### 2. 현재 데이터 구조
```text
.
├── data/                   # 원본 PDF 파일 (Git 제외)
├── final_output/           # Marker 변환 결과 (.md, 이미지 등)
├── scripts/                # 데이터 가공용 파이썬 스크립트
├── requirements.txt        # 환경 설정 파일
└── README.md               # 프로젝트 가이드
```
___

## **설치 및 실행 방법 (다른 컴퓨터용)**

사양이 낮은 데스크톱이나 새로운 환경에서 프로젝트를 실행할 때 아래 순서를 따르세요.

1. 가상환경 설정

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

```

2. 의존성 설치

```bash
pip install -r requirements.txt
```

3. PDF 변환 (새로운 문서 추가시)

```bash
# 단일 파일 변환
marker_single data/FILENAME.pdf --output_dir ./final_output --langs Korean,English
```

___

## 📅 향후 계획 (To-Do)
앞으로 데이터의 정확도를 높이고 LLM 분석을 적용하기 위해 다음 단계를 진행할 예정입니다.

1. 데이터 청킹(Chunking) 최적화:

    * 500페이지 텍스트를 LLM 컨텍스트 윈도우에 맞게 섹션(Heading)별로 자동 분할하는 스크립트 작성.

2. 표 데이터 정제(Post-processing):

    * 마크다운 내의 표 데이터를 추출하여 엑셀(CSV) 형식으로 자동 변환 및 정규화.

3. RAG(Retrieval-Augmented Generation) 시스템 구축:

    * 추출된 데이터를 벡터 DB에 저장하여 정부 보고서 기반 질의응답 시스템 구현.

4. LLM 가공:

    * Gemini/GPT API를 연동하여 복잡한 통계 수치에 대한 자동 요약 및 인사이트 도출.

___

## ⚠️ 주의사항

* 용량 관리: 원본 PDF 및 추출된 이미지 자산은 용량이 크므로 Git Push 시 제외( .gitignore 설정 필수).

* 연산 자원: 500페이지 이상의 대용량 파일 변환 시 CPU/GPU 점유율이 높으므로 caffeinate 등을 통해 잠자기 모드 방지 권장.

___

### 💡 추가 제안: `.gitignore` 설정
README를 만드셨다면, 대용량 파일이 깃허브에 올라가지 않도록 폴더에 **`.gitignore`** 파일도 만들어서 아래 내용을 꼭 넣어주세요.

```text
.venv/
data/*.pdf
final_output/
__pycache__/
.DS_Store
```