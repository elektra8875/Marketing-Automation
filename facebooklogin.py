from selenium import webdriver

# open Firefox browser and go to facebook login page

browser = webdriver.Firefox()
browser.get('https://www.facebook.com')

# find input field and enter my username

UserElem = browser.find_element_by_id('email')
UserElem.send_keys('mistressmichele75@gmail.com')

# find password input field and enter password

PassElem = browser.find_element_by_id('pass')
PassElem.send_keys('Mangohill 215$')

# Find login button and click it

LoginElem = browser.find_element_by_id('u_0_8')
LoginElem.click()
