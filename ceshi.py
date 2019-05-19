from selenium import webdriver
import time


driver_path = r"E:\chromedeiver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')

time.sleep(5)
driver.close()
driver.quit()
