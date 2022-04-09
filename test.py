from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
chrome_options = ChromeOptions()
chrome_options.add_extension('test_src.crx')


driver = webdriver.Chrome('D:/chromedriver/chromedriver', options = chrome_options)
driver.get('https://google.com')
sleep(3)
driver.get('https://youtube.com')
sleep(3)
driver.get('chrome-extension://hhgbhcehbginhikalilbcpbpfedhnaag/analysis.html')
sleep(3)
driver.get('chrome-extension://hhgbhcehbginhikalilbcpbpfedhnaag/popup.html')
print("test has finished!")
driver.quit()
