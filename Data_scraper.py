from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

chrome_driver=r"D:\VSCode Data\chromedriver-win64\chromedriver.exe"
service=Service(chrome_driver)
driver=webdriver.Chrome(service=service)

driver.get('https://stackoverflow.com/')
element = driver.find_element(By.NAME, 'q')
element.click()
element.send_keys("switch for python")
element.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'answer-hyperlink')))

urls=[]
while True:
    element = driver.find_elements(By.CLASS_NAME, 'answer-hyperlink')
    for url in element:
        urls.append(url.get_attribute('href'))
    try:
        element = driver.find_element(By.LINK_TEXT, 'Next')
        element.click()
    except:
        print("No more pages....")
        break

for i, url in enumerate(urls):
        print(f"Link #{i+1}: {url}")
print ("Results displayed. Exiting the automation.")
driver.quit()

excel_file_save_path=r"D:\VSCode Data\Data_scraper.xlsx"
df=pd.DataFrame(urls,columns=["Links STACKOVERFLOW"])
df.to_excel(excel_file_save_path,index=False)
print(f"File saved at {excel_file_save_path}")
