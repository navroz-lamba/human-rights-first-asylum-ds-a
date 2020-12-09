from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

import random




col_names = ["URLS"]
urls = pd.read_csv('output.csv', names=col_names)
for x in range(len(urls)):
    urls["URLS"][x] = urls["URLS"][x].replace("'", " ")

urls2 = []


#getting rid of all non scribd links
for x in range(len(urls)):
    if "www.scribd.com" in urls["URLS"][x]:
        urls2.append(urls["URLS"][x])
    else:
        continue

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {#change this to your desired directory
"download.default_directory": r"C:\Users\lesle\Desktop\lambda\labs pdfs\pdfs",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": False
})
#need a chrome webdriver here
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\lesle\Desktop\lambda\labs pdfs\chromedriver.exe')

#initial sign in path
path = urls2[2000]

driver.get(path)

driver.get_window_position()

xpath = '//*[@id="reading_progress_container"]/div[3]/div[1]/div/button/span'

btn = driver.find_element_by_xpath(xpath)
#login click
btn.click()

xpath2 = '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/a'
#other login click
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/a'))).click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/a'))).click()


#login email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_or_email"]'))).click()
element = driver.find_element_by_xpath('//*[@id="login_or_email"]')
element.send_keys("yourmailheer@gmail.com")
#login password
element = driver.find_element_by_xpath('//*[@id="login_password"]')
element.send_keys("password")



#clicks on sign in
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/form/fieldset/div[3]/button'))).click()

#clicks on download button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/a'))).click()

time.sleep(10)



for x in range(2000, 2500):


        path = urls2[x]

        print(path)

#goes to URL
        driver.get(path)


        driver.get_window_position()
#clicks on download button
        xpath = '/html/body/div/div/div[4]/div/div[2]/section/div/div[1]/div[3]/div[1]/div/button/span'

        btn = driver.find_element_by_xpath(xpath)

        btn.click()
#clicks on next download button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/a'))).click()
#sleep to try and trick the script detection, doesn't work though
        time.sleep(120)
