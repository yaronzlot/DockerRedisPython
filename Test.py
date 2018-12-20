import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:/temp/chromedriver.exe")


# Enter the web site
driver.get("http://192.168.99.100:5000")
driver.maximize_window()
driver.implicitly_wait(60)

# print the message
msg = driver.find_element_by_css_selector("body").text
print(msg)
driver.quit()


