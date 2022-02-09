import json
import sys
from selenium import webdriver

PATH = 'C:\\Users\\jopr299\\Desktop\\Selenium-Übungen\\geckodriver.exe'

driver = webdriver.Firefox()
driver.get('https://de.wikipedia.org/wiki/Wikipedia:Hauptseite')















# from testdata import data
# data_json = json.dumps(data)
# print(data_json)

# sys.stdout.flush()