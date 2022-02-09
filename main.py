import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# Get the geckodriver from the PATH-Variables
PATH = os.environ.get('geckodriver.exe')

# Create the driver
driver = webdriver.Firefox()

# Open the Wikipedia-Mainpage
driver.get('https://de.wikipedia.org/wiki/Wikipedia:Hauptseite')
print(driver.title)

# Find the div of the article of the day
article = driver.find_element(By.ID,'artikel')
print("Hauptartikel:")
print(article)


print("---------------")

# Find the div which has the anchor element of the link in it
hauptseite_mehr = driver.find_element(By.CLASS_NAME, 'hauptseite-mehr')
print(hauptseite_mehr.text)
driver.quit()















# from testdata import data
# data_json = json.dumps(data)
# print(data_json)

# sys.stdout.flush()