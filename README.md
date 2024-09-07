# Web-Indexing_Currency

## 개요
Selenium 활용 웹 크롤링을 통한 환율 정보 사이트 Flask를 활용해 웹 상에 결과가 표시되도록 구현

## 주요 기능
- **특정 국가 환율 조회**: 사용자가 메인 페이지에서 특정 국가의 이름을 입력하면, 해당 국가의 매매기준율, 현찰환율, 송금환율을 웹에서 크롤링하여 테이블 형식으로 표시, 외화 -> 원화 환전 기능 제공
- **전체 국가 환율 조회**: 사용자가 메인 페이지에서 전체국가 환율 보기를 클릭하면, 모든 국가의 환율 정보를 웹에서 크롤링해 테이블 형태로 보여주고 국가별로 더 많은 정보를 볼 수 있는 페이지로의 이동 기능 제공

## 크롤링 사이트 
- 특정 국가 환율 조회: 다음 검색 - 환율+국가명 [예시](https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=환율미국)
- 전체 국가 환율 조회: [네이버 페이 증권 - 환율](https://m.stock.naver.com/marketindex/home/exchangeRate/exchange#exchange)
## 파일 설명
### app.py - Flask 애플리케이션 파일, 크롤링 및 템플릿 랜더링 수행
### currency.html - 특정 국가 환율 조회 페이지 템플릿
### currency_all.html - 전체 국가 환율 조회 페이지 템플릿
### index.html - 메인 페이지 템플릿

## 실행 결과
![image](https://github.com/user-attachments/assets/74bb745b-239f-41af-9d9c-0045b2bca7ab)
![image](https://github.com/user-attachments/assets/dbf65598-b724-48b6-aa5b-7463b1c6e106)
![image](https://github.com/user-attachments/assets/3d77b467-ca1a-4fdf-a7e4-fce8c308c890)
