from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/')
def result():
    url = 'https://m.stock.naver.com/marketindex/home/exchangeRate/exchange#exchange'
    driver = webdriver.Edge()

    driver.get(url)
    driver.implicitly_wait(10)

    rows = driver.find_elements(By.XPATH, '//div[contains(@class, "Table_tableArea__IGE30")]/table/tbody/tr')

    app_data = []

    for row in rows:
        country = row.find_element(By.XPATH, './td[1]//span[contains(@class,"Table_name__ghHRg")]').text
        time = row.find_element(By.XPATH, './td[1]//time').text
        rate = row.find_element(By.XPATH, './td[2]').text.split('\n')[0]
        gap = row.find_element(By.XPATH, './td[2]//div[contains(@class, "StockGap_stockGap")]').text
        gap_percent = row.find_element(By.XPATH, './td[3]//div[contains(@class, "StockGap_stockGap")]').text

        data_row = {
            "time": time,
            "country": country,
            "rate": rate,
            "gap": gap,
            "gap_percent": gap_percent
        }
        app_data.append(data_row)

    driver.quit()

    return render_template('index.html', app=app_data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')
