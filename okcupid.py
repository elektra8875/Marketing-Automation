
from selenium import webdriver
import time

# open Firefox browser and go to okcupid login page

browser = webdriver.Firefox()
browser.get('https://www.okcupid.com/login')


# find Email Input and insert username

UserElem = browser.find_element_by_name('username')
UserElem.send_keys('katiamistress75@gmail.com')

# Find password input and enter password

PassElem = browser.find_element_by_name('password')
PassElem.send_keys('Mangohill 215')

# find Log In button and click on it

LogButton = browser.find_element_by_class_name('login2017-actions-button')
LogButton.click()

# 60 second time delay

time.sleep(30) 


browser.get('https://www.okcupid.com/logout')

#close browser

browser.quit()
