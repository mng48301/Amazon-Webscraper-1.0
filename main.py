import selenium
import time
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#databases
title_data = []
prices_data = []
rating_data = []

def webscrape(prompt):
    
    driver = webdriver.Chrome()
    driver.maximize_window()

    #prompt search
    driver.get("https://www.amazon.com/")
    sleep(5)
    searchbox = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    sleep(1)
    searchbox.click()
    searchbox.send_keys(prompt)
    searchfunc = driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
    searchfunc.click()

    #scraping page

    #title
    wait = WebDriverWait(driver, 5)
    titles = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "h2")))
    tracker = 0                                                                                   

    for title in titles: 
        if tracker + 1 < len(titles):
            title_data.append(title.text)
            tracker = tracker + 1
        else:
            break
    #price
    tracker = 0
    prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price") #a-price

    for price in prices:
        if tracker <= len(prices):
            if "b" in price.get_attribute("data-a-size"):
                continue
            price_text = price.text
            if len(price.text) <= 5:
                price_text = price.text + " "
            tracker = tracker + 1
            prices_data.append(price_text.replace("\n", "."))
    

    #rating
    tracker = 0
    ratings = driver.find_elements(By.CLASS_NAME, "a-popover-trigger.a-declarative span.a-icon-alt")
    for rate in ratings:
        if tracker < len(ratings) and tracker < len(titles):
            rating_text = rate.get_attribute("innerHTML")
            rating_data.append(rating_text.replace(" out of 5 stars", "/5"))
            tracker = tracker + 1
        else:
            rating_data.append("N/A")
  
   


    #print all --------------------------------------
    os.system('cls')
  
 
    #statistics
    count = 0
    total_rate = 0
    total_price = 0

    for price in prices_data:  
        if price.strip():
            total_price += float(price.replace("$", "").replace("\n", ""))
    average_price = total_price / len(prices_data)

    for rate in rating_data:
        if rate != "N/A":
            real_rate = rate.replace("/5", "")
            total_rate += float(real_rate)
            count += 1
    if count > 0:
        average_rate = total_rate / count
    else: 
        average_rate = "insufficient ratings"


    print("               ___________")
    print("              |STATISTICS |")
    print("               -----------")
    print("Average Price: "); print(average_price)
    print("Average Rating: "); print(average_rate)


    #data table
    print(" ____________________________________________________ ")
    print("|    PRODUCT TITLE     |     PRICE    |    RATING    |")
    for row in range(0, len(rating_data)):
        if not title_data[row]:
            row += 1
        message = "|    " + title_data[row][0:15] + "   |     " + prices_data[row] + "   |     " + rating_data[row] + "    |"
        print(message)
    
    sleep (1000)


#main
os.system('cls')
print(r"                             ____    ___ ")
print(r"                \\ /\  //   ||___    |__|")
print(r"                 \\//\\/    ||___    |__|")
print(r"                 ---AMAZON WEBSCRAPER--- ")
print("created by: Max Glisky")
print("version 1.0\n")
prompt = input("Enter prompt: ")

webscrape(prompt)
