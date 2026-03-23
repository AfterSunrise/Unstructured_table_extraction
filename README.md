# 📊 Unstructured Table & Figure Extraction
이 프로젝트는 unstructured 라이브러리를 사용하여 PDF 문서 내의 **표(Table)**를 HTML로 변환하고, **그림(Figure/Image)**을 별도 파일로 추출하는 도구입니다.

## 🛠 1. 시스템 의존성 설치 (System Dependencies)
이 라이브러리는 내부적으로 OCR과 PDF 렌더링 엔진을 사용하므로, OS별로 아래 도구들을 먼저 설치해야 합니다.

### 🍎 macOS (MacBook)
터미널에서 Homebrew를 사용해 설치합니다.

```Bash
brew install tesseract poppler
```
한국어 OCR이 필요하다면: brew install tesseract-lang (또는 기본 설치에 포함됨)

### Windows
#### 방법 A: winget 사용 (권장)
관리자 권한의 PowerShell에서 실행합니다.

```PowerShell
# Tesseract OCR 설치
winget install UB-Mannheim.TesseractOCR

# Poppler 설치
# Poppler는 직접 다운로드가 가장 확실합니다.
# https://github.com/oschwartz10612/poppler-windows/releases 에서 최신 bin 폴더 압축 해제
```
#### 방법 B: 수동 설치 및 환경 변수 설정

Tesseract: 설치 파일 실행 시 Korean 언어 팩을 체크하여 설치합니다.

Poppler: 압축을 푼 뒤 bin 폴더 경로를 시스템 환경 변수 Path에 추가합니다.
___

## 🐍 2. 파이썬 환경 설정
프로젝트 폴더에서 가상환경을 만들고 필요한 패키지를 설치합니다.

```Bash
# 1. 가상환경 생성
python -m venv venv

# 2. 가상환경 활성화
# (macOS/Linux)
source venv/bin/activate
# (Windows)
venv\Scripts\activate

# 3. 필수 패키지 설치
pip install -r requirements.txt
```
___

## 🚀 3. 실행 방법
main.py (또는 작성하신 파일명)를 실행하면 extracted_figures/ 폴더에 그림이 저장되고, 표 데이터가 터미널에 출력됩니다.

```Bash
python main.py
```
___

## 📂 4. 파일 구조 (Requirements.txt)
requirements.txt 파일에는 아래 내용이 포함되어야 합니다.

```Plaintext
unstructured[all-docs]>=0.12.0
pdf2image
pdfminer.six
pi-heif
pytesseract
opencv-python
pillow
layoutparser
torch
torchvision
onnxruntime
```
___

# ⚠️ 주의사항 (Troubleshooting)
1. Windows Tesseract 경로 에러:
만약 TesseractNotFoundError가 발생하면 코드 상단에 설치 경로를 직접 명시하세요.

```Python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
2. Poppler 에러:
PDF를 이미지로 변환하지 못한다는 에러가 뜨면 Poppler의 bin 폴더가 환경 변수에 잘 잡혀 있는지 확인하세요.

3 한글 인식:
partition_pdf 함수 호출 시 languages=["kor", "eng"] 옵션이 설정되어 있는지 확인하세요.