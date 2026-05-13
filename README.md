# YOLOv8 커스텀 객체 탐지 프로젝트

## 프로젝트 소개

YOLOv8 기반 객체 탐지 모델 학습을 위해  
데이터 전처리부터 커스텀 학습까지 직접 구현한 프로젝트입니다.

이 프로젝트에서는 다음 과정을 직접 구현했습니다.

- pretrained YOLOv8 모델 추론
- 특정 클래스(person) 라벨 추출
- 클래스 번호 변환
- 라벨 병합 자동화
- train / validation 데이터 분리
- YOLOv8 커스텀 학습

객체 탐지 모델 학습 과정과 데이터 전처리 흐름을 이해하는 것을 목표로 진행했습니다.

<img width="3940" height="1920" alt="mergepictures net-merged-1778696029  (1)" src="https://github.com/user-attachments/assets/489882f3-33a8-4492-bc98-08d5a30890db" />

<img width="1698" height="490" alt="KakaoTalk_20260514_031943276" src="https://github.com/user-attachments/assets/ce7813de-bce7-4b94-ac13-6060184fe2fc" />


---

## 주요 기능

### 1. 클래스 라벨 변환

`Class_converter.py`

- YOLOv8 추론 결과에서 person 클래스만 추출
- 클래스 번호 변경
- 새로운 라벨 파일 생성

예시:

```txt
0 x_center y_center width height
↓
2 x_center y_center width height
```

---

### 2. 라벨 병합 자동화

`Merge_label.py`

- 변환된 라벨을 기존 데이터셋 라벨에 자동 병합
- annotation 수작업 최소화

---

### 3. 데이터셋 분리 및 설정

`Custom_train.py`

- train / validation 데이터 자동 분리
- `data.yaml` 자동 수정
- YOLOv8 학습 환경 구성

---

### 4. YOLOv8 커스텀 학습

`YoloV8.ipynb`

- 커스텀 데이터셋 학습
- 모델 추론 및 실험 진행

---

## 사용 기술

- Python
- YOLOv8
- Ultralytics
- Scikit-learn
- YAML

---

## 프로젝트를 통해 배운 점

- YOLO annotation 구조 이해
- 객체 탐지 데이터 전처리 과정
- 커스텀 데이터셋 구성 방법
- 라벨 자동화 및 데이터 관리
- YOLOv8 학습 파이프라인 구축

---

## 전체 작업 흐름

```text
Pretrained YOLOv8 추론
            ↓
특정 클래스 라벨 추출
            ↓
라벨 변환 및 병합
            ↓
Train / Validation 데이터 구성
            ↓
커스텀 YOLOv8 모델 학습
```

---

## 개선 예정 사항

- 라벨 시각화 기능 추가
- 다중 클래스 지원
- 데이터 증강 자동화
- 전체 학습 과정 자동화
