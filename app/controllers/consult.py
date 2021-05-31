from app import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@app.route("/stocks", methods=['GET'])
def stocks():

  region = 'Argentina'


  url = 'https://www.coronatracker.com/pt-br'

  driver = webdriver.chrome()
  driver.get(url)










  result = 'aaaaaaaaaaaaaaaaa'

  return jsonify(result)


