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
link = driver.find_element(By.LINK_TEXT, hauptseite_mehr.text)
print(link)


# Accessing the page of the articel of the day:
link.click()

# Accessing and printing the p-element of the article
first_P = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/p[1]')
print('----------------')
print(first_P.text)


def fill_result(link, n):
    current_link = link
    result = []

    return None



# Close the driver
driver.quit()









# from testdata import data
# data_json = json.dumps(data)
# print(data_json)

# sys.stdout.flush()