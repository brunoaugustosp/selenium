from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from time import sleep


url = 'https://www.coronatracker.com/pt-br'

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(url)

sleep(5)
cases = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a')
casestext = cases.text


print(casestext)

