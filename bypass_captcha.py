#system libraries
import os
import random
import time
#selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options


#recaptcha libraries
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub


def delay():
    time.sleep(random.randint(2, 3))


try:
    # create chrome driver
    driver = webdriver.Chrome(os.getcwd() + "\\webdriver\\chromedriver.exe")
    delay()
    # go to website
    driver.get("https://www.google.com/recaptcha/api2/demo")

except:
    print("[-] Please update the chromedriver.exe")