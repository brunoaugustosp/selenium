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
    element01 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click()
    sleep(1)
    element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
    sleep(1)
    find = driver.find_element_by_xpath(f'//span[text()="{self.region}"]').click()
    sleep(2)
    element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()
    sleep(3)
    show_rows = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[2]/span/div/span/span').click()
    sleep(1)
    volume_rows = driver.find_element_by_xpath(f'//span[text()="Show 100 rows"]').click()
    sleep(3)

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
        next = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[2]/button[3]/span/span').click()
        sleep(3)
    driver.quit()

    
    return jsonify(stocks)
