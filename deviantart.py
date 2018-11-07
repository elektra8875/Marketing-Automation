from selenium import webdriver
import pyautogui

# open Firefox browser and go to DeviantArt login page

browser = webdriver.Firefox()
browser.get('https://www.deviantart.com/users/login')


# find username or Email Input and insert username

UserElem = browser.find_element_by_id('login_username')
UserElem.send_keys('KatiaMistress')

# Find password input and enter password

PassElem = browser.find_element_by_id('login_password')
PassElem.send_keys('Mangohill215')

# find Log In button and click on it

LogButton = browser.find_element_by_class_name('smbutton.smbutton-size-default.smbutton-shadow.smbutton-blue')
LogButton.click() 

# go to the submit page and press submit

browser.get('https://www.deviantart.com/submit/deviation')

#width, height = pyautogui.size()
#print(width, height)
#
import time
time.sleep(1)

pyautogui.click(360,231)
time.sleep(3)

#click on submit button and upload image from desktop

#FileUploadElem = browser.find_element_by_xpath('//*[@id="/dapi/v1/submit/upload"]')
#FileUploadElem.click()
#
#FileUploadElem.send_keys(r"C:\Users\Cindy\Desktop\cindfemdom.jpg")
#
## find the Save and Exit button and click
#
#SaveExit = browser.find_element_by_id("ile-button.ile-handicapped.ile-save-exit-button.smbutton.smbutton-white")
#SaveExit.click()

# close browser

browser.quit() 



