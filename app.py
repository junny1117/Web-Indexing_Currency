from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/currency', methods=['GET'])
def currency():
    query = request.args.get('country')
    url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=환율{}'.format(query)
    
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@class="f_etit"]'))
    )

    country = driver.find_element(By.XPATH, '//a[@class="f_etit"]').text.strip()
    rate = driver.find_element(By.XPATH, '//em[@class="txt_num"]').text.strip()
    time_info = driver.find_element(By.XPATH, '//*[@id="exchangeColl"]/div[3]/div/div[3]/div[2]/div[2]/span[1]').text.strip()
    gap_element = driver.find_element(By.XPATH, '//dl[@class="dl_comm"]/dd[1]').text.strip()
    gap = gap_element.split()[-1]  
    gap_percent = driver.find_element(By.XPATH, '//dl[@class="dl_comm"]/dd[2]').text.strip()

    buy = driver.find_element(By.XPATH, '//td[text()="살 때"]/following-sibling::td').text.strip()
    sell = driver.find_element(By.XPATH, '//td[text()="팔 때"]/following-sibling::td').text.strip()
    send = driver.find_element(By.XPATH, '//td[text()="보낼 때"]/following-sibling::td').text.strip()
    receive = driver.find_element(By.XPATH, '//td[text()="받을 때"]/following-sibling::td').text.strip()

    app_data2 = {
        "country": country,
        "rate": rate,
        "gap": gap,
        "gap_percent": gap_percent,
        "buy": buy,
        "sell": sell,
        "send": send,
        "receive": receive,
        "time": time_info
    }

    driver.quit()
        
    return render_template('currency.html', app=app_data2)

@app.route('/currency_all')
def currency_all():
    url = 'https://m.stock.naver.com/marketindex/home/exchangeRate/exchange#exchange'
    
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    
    driver.get(url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "Table_tableArea__IGE30")]/table/tbody/tr'))
    )

    rows = driver.find_elements(By.XPATH, '//div[contains(@class, "Table_tableArea__IGE30")]/table/tbody/tr')

    app_data = []

    for row in rows:
        country = row.find_element(By.XPATH, './td[1]//span[contains(@class,"Table_name__ghHRg")]').text
        time_info = row.find_element(By.XPATH, './td[1]//time').text
        rate = row.find_element(By.XPATH, './td[2]').text.split('\n')[0]
        gap = row.find_element(By.XPATH, './td[2]//div[contains(@class, "StockGap_stockGap")]').text
        gap_percent = row.find_element(By.XPATH, './td[3]//div[contains(@class, "StockGap_stockGap")]').text

        data_row = {
            "time": time_info,
            "country": country,
            "rate": rate,
            "gap": gap,
            "gap_percent": gap_percent
        }
        app_data.append(data_row)

    driver.quit()
    return render_template('currency_all.html', app=app_data)


