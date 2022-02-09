import json
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = 'C:\\Users\\jopr299\\Desktop\\Selenium-Übungen\\geckodriver.exe'

driver = webdriver.Firefox()
driver.get('https://de.wikipedia.org/wiki/Wikipedia:Hauptseite')
print(driver.title)
article = driver.find_element(By.ID,'artikel')
print("Hauptartikel:")
print(article)
print("---------------")
hauptseite_mehr = driver.find_element(By.CLASS_NAME, 'hauptseite-mehr')
print("LINK:")
print(hauptseite_mehr.text)
driver.quit()















# from testdata import data
# data_json = json.dumps(data)
# print(data_json)

# sys.stdout.flush()