# Web-Indexing_Currency

## 개요

- Selenium 활용 웹 크롤링을 통한 환율 정보 사이트 
- Flask를 활용해 웹 상에 결과가 표시되도록 구현

## 주요 기능

- **특정 국가 환율 조회**: 사용자가 메인 페이지에서 특정 국가의 이름을 입력하면, 해당 국가의 매매기준율, 현찰환율, 송금환율을 웹에서 크롤링하여 테이블 형식으로 표시, 외화 -> 원화 환전 기능 제공
- **전체 국가 환율 조회**: 사용자가 메인 페이지에서 전체국가 환율 보기를 클릭하면, 모든 국가의 환율 정보를 웹에서 크롤링해 테이블 형태로 보여주고 국가별로 더 많은 정보를 볼 수 있는 페이지로의 이동 기능 제공

## 크롤링 사이트 

- 특정 국가 환율 조회: 다음 검색 - 환율+국가명 [예시](https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=환율미국)
- 전체 국가 환율 조회: [네이버 페이 증권 - 환율](https://m.stock.naver.com/marketindex/home/exchangeRate/exchange#exchange)


## 사용도구/기술 

- **Python**: 개발언어
- **Selenium**: 웹 크롤링
- **Flask**: 웹 기반 인터페이스
- **HTML, CSS, Bootstrap**: 웹패이지 템플릿
- **Visual Studio Code**: 코드 작성
- **Windows**: 운영체제

## 파일 목록

### app.py - Flask 애플리케이션 파일, 크롤링 및 템플릿 랜더링 수행
### currency.html - 특정 국가 환율 조회 페이지 템플릿
### currency_all.html - 전체 국가 환율 조회 페이지 템플릿
### index.html - 메인 페이지 템플릿
### requirements.txt - 실행에 필요한 패키지 목록

## 실행 방법

1. 프로젝트 클론: `git clone https://github.com/junny1117/Web-Indexing_Currency`
2. 필요한 패키지 설치: `pip install -r requirements.txt`
3. Flask 서버 실행: `flask run`
4. 브라우저에서 `127.0.0.1:5000`으로 접속

## 실행 결과
![스크린샷 2024-10-22 113414](https://github.com/user-attachments/assets/04f5ae9e-4bf2-4092-8784-5230cacb98fa)
![스크린샷 2024-10-22 113526](https://github.com/user-attachments/assets/08189d71-255b-4752-a208-3f5ceac16012)
![스크린샷 2024-10-22 113631](https://github.com/user-attachments/assets/6a1ef63f-2587-4996-b2ee-2a5c2e5153ea)



