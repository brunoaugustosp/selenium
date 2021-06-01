from selenium import webdriver
from selenium.webdriver.chrome.options import *
import os

from time import sleep




driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://finance.yahoo.com/screener/new')



element01 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click()
element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
find = driver.find_element_by_xpath('//span[text()="Argentina"]').click()
sleep(2)
element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()
sleep(2)



row = 1
while row <= 25:

    estimated_result = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[2]/div/div[2]/div').text
    symbol = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[1]/a').text
    name = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[2]').text
    price = driver.find_element_by_xpath(f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{row}]/td[3]/span').text

    print(estimated_result)
    print(symbol)
    print(name)
    print(price)
    row += 1





print(estimated_result)
print(symbol)
print(name)
print(price)


