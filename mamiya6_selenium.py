import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# I did naht hit her, it's bowshit, it's not true, I did naht hit her, I did NAHHHT
# Oh hi Stephen

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get('https://kenrockwell.com/')
time.sleep(2)
search_box = driver.find_element("id", "Search").click()
time.sleep(2)

tele = driver.find_element("name", "q") # finds search box


tele.send_keys("Mamiya 6")
time.sleep(2)

tele.send_keys(Keys.RETURN)

click_link = driver.find_element(By.XPATH, "//div[@id='rso']/div/div/div/div/div/div/a/h3").click()




time.sleep(5)