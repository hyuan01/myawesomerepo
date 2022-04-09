from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
import pytest
chrome_options = ChromeOptions()
chrome_options.add_extension('test_src.crx')

def run_selenium():
    driver = webdriver.Chrome('D:/chromedriver/chromedriver', options = chrome_options)
    driver.get('https://google.com')
    sleep(3)
    driver.get('https://youtube.com')
    sleep(3)
    #driver.get('chrome-extension://<YOUR UNIQUE ID HERE>/analysis.html')
    #sleep(3)
    #driver.get('chrome-extension://<YOUR UNIQUE ID HERE>/popup.html')
    #input('Press [Enter] To close browser')
    driver.quit()
    print("done testing selenium")
    return True

def test_selenium():
    assert run_selenium()