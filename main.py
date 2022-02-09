import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# Get the geckodriver from the PATH-Variables
PATH = os.environ.get('geckodriver.exe')

# Wikipedia-Paths:
first_p_path = '/html/body/div[3]/div[3]/div[5]/div[1]/p[1]'
first_a_path = first_p_path + '/a[1]'
title_id = 'firstHeading'
wikipedia_homepage = 'https://de.wikipedia.org/wiki/Wikipedia:Hauptseite'
article_of_the_day_id = 'artikel'



# Create the driver
driver = webdriver.Firefox()

# Open the Wikipedia-Mainpage
driver.get(wikipedia_homepage)

# Find the div of the article of the day
article = driver.find_element(By.ID, article_of_the_day_id)


# Find the div which has the anchor element of the link in it
hauptseite_mehr = driver.find_element(By.CLASS_NAME, 'hauptseite-mehr')

# Link to the article of the day
link = driver.find_element(By.LINK_TEXT, hauptseite_mehr.text)


def fill_result(link, n):
    current_link = link
    result = []

    #Iterating through the pages:
    for i in range(n):

        # Accessing the page:
        current_link.click()

        #Printing the actual page-link:
        print('-----PAGE LINK:--------')
        print(current_link.get_attribute('href'))

        # Accessing and printing the title of the article
        title = driver.find_element(By.ID, title_id)
        title_text = title.text
        #print('----------------')
        #print('TITLE:')
        #print(title_text)

        # Accessing and printing the p-element of the article
        first_p_elem = driver.find_element(By.XPATH, first_p_path)
        p_text = first_p_elem.text
        #print('----------------')
        #print('TEXT:')
        #print(p_text)

        # Accesing a random link to a new wikipedia page and assign it to the current_link variable
        current_link = driver.find_element(By.XPATH, first_a_path)

        result.append({'title':title_text, 'p-text':p_text})
    
    return result

        
result = fill_result(link, 10)
#print(result)


# Close the driver
driver.quit()









# from testdata import data
# data_json = json.dumps(data)
# print(data_json)

# sys.stdout.flush()