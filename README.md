# Web-Indexing_Currency

## 개요

- Selenium을 이용한 ​웹 크롤링 활용​ 환율 정보 사이트​ 

## 구현 사항

- **특정 국가 환율 조회**: **사용자**가 **메인 페이지**에서 **국가명**을 입력하면, 해당 국가의 **매매기준율**, **현찰환율**, **송금환율**을 웹에서 **크롤링**하여 **테이블 형태**로 표출, **외화 -> 원화** 환전 기능 제공
- **전체 국가 환율 조회**: **사용자**가 **메인 페이지**에서 **전체국가 환율 보기**를 **클릭**하면, 전체 국가의 **환율 정보**를 웹에서 **크롤링**해 **테이블 형태**로 표출하고 각 국가별로 더 많은 정보를 확인할 수 있는 **특정 국가 환율 조회 페이지**로의 **이동 기능** 제공

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



