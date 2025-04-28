# QA 포트폴리오 - API 테스트 프로젝트

## 📌 프로젝트 소개
- 테스트 대상: [https://reqres.in](https://reqres.in)
- Reqres API 기반 Python API 테스트 자동화
- pytest + requests 라이브러리 사용
- 기능별 모듈화 (auth, user, resource)

## 프로젝트 구조
```
qa_api_project/
├── api_tests/ (API 호출 함수)
├── tests/ (pytest 테스트 케이스)
├── requirements.txt
├── pytest.ini
└── setup.py
```

## 📋 수행 항목
1. login
2. register
3. users
4. resoruce

## 실행 방법
1. 패키지 설치
    ```
    pip install -r requirements.txt
    ```
2. 테스트 실행
    ```
    pytest --html=report.html
    ```
    
## 기술 스택
- Python 3.12.2
- requests
- pytest
- pytest-html (리포트 생성)

