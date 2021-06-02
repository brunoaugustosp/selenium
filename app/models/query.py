from logging import exception
from selenium import webdriver
from selenium.webdriver.chrome.options import *
import os
from flask import jsonify
from time import sleep



class Stock:


  def __init__(self,region):

    self.region = region

  def web_crawler(self):

    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.get('https://finance.yahoo.com/screener/new')
    sleep(4)
    btn_reg = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click()
    sleep(4)
    add_region = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
    sleep(4)
    select_region = driver.find_element_by_xpath(f'//span[text()="{self.region}"]').click()
    sleep(4)
    find_stock = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()
    sleep(4)
    show_rows = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[2]/span/div/span/span').click()
    sleep(4)
    show_100_rows = driver.find_element_by_xpath(f'//span[text()="Show 100 rows"]').click()
    sleep(4)

    stocks = []

    while True:
        try:
          row = 1
          while row <= 100:
            symbol = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[1]/a').text
            name = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[2]').text
            price = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[3]/span').text

            print(symbol)
            print(name)
            print(price)

            stocks.append({symbol:{
              "symbol": symbol,
              "name": name,
              "price": price
            }})
          
            row += 1
        except:
          break

        
        next_page = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[2]/button[3]/span/span').click()
        sleep(4)
        

    driver.quit()

    return jsonify(stocks)
