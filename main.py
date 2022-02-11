import json
from logging import exception
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# from testdata import data

#Quantity of pages that shall be crawled
page_quantity = 10

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

# Method to iterate through a bunch of Wikipedia-pages
#
# @param link_to_page: an anchor-element which is the start-point of the iteration
# @param n: quantity of iterations
#
# @return: list of objects containing title, first part of the text, url of the main-image and the link to the page

def fill_result(link_to_page, n):
    current_link = link_to_page
    result = []
    try:
        #Iterating through the pages:
        for i in range(n):

            # Accessing the current link as a plain string
            href = current_link.get_attribute("href")

            # Accessing the page:
            current_link.click()

            # Accessing and the title of the article
            title = driver.find_element(By.ID, title_id)
            title_text = title.text

            # Accessing the first p-element of the article
            first_p_elem = driver.find_element(By.XPATH, first_p_path)
            p_text = first_p_elem.text

            # Accessing the path of the main image:
            images = driver.find_elements(By.CLASS_NAME, 'thumbimage')

            main_img = ""
            main_img_url = ""
            
            if len(images) != 0:
                main_img = driver.find_element(By.CLASS_NAME, 'thumbimage')
                main_img_url = main_img.get_attribute('src')



            # Accesing a random link to a new wikipedia page and assign it to the current_link variable
            page_link = driver.find_element(By.XPATH, first_a_path)
            current_link = page_link


            # Filling the result:
            result.append({'title':title_text, 'p-text':p_text, 'link': href, 'img': main_img_url})
    except Exception as e:
        return result

    return result

        
result = fill_result(link, page_quantity)


# Close the driver
driver.quit()

# Converting the result to JSON-format
result_json = json.dumps(result)

# Printing the JSON
print(result_json)
sys.stdout.flush()