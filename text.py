from selenium import webdriver
from selenium.webdriver.chrome.options import *
import os

from time import sleep


url = 'https://finance.yahoo.com/screener/new'

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(url)



element01 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click()
element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
element02 = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
sleep(1)
find = driver.find_elements_by_xpath("//*[label[text()='Argentina']]/input").click()


sleep(25)

estimated_result = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[2]/div/div[2]/div').text

symbol = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a').text
name = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[2]').text
price = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[3]/span').text






print(estimated_result)
print(symbol)
print(name)
print(price)


