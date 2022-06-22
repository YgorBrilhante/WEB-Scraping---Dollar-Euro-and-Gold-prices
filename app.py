# Automação WEB (WEB - Scraping)
# Search for dollar, euro and gold prices


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.google.com/")

browser.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

browser.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dollar_price = browser.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(dollar_price)


browser.get("https://www.google.com/")
browser.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
browser.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

euro_price = browser.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(euro_price)


browser.get("https://www.melhorcambio.com/ouro-hoje")

gold_price = browser.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
gold_price = gold_price.replace(",", ".")
print(gold_price)

browser.quit()