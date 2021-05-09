from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException   
import time


PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://play.typeracer.com/")

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

time.sleep(3)
body = driver.find_element_by_class_name("redesign")
body.send_keys(Keys.CONTROL, Keys.ALT, "O")

time.sleep(5)

firsttext = driver.find_element_by_xpath("//*[@id='gwt-uid-20']/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]").get_attribute('innerHTML')
secondtext = driver.find_element_by_xpath("//*[@id='gwt-uid-20']/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]").get_attribute('innerHTML')
thirdtext = ""

if check_exists_by_xpath("//*[@id='gwt-uid-20']/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]"):
    thirdtext = driver.find_element_by_xpath("//*[@id='gwt-uid-20']/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]").get_attribute('innerHTML')


fulltext = firsttext + secondtext + thirdtext

print(fulltext)

inputfield = driver.find_element_by_class_name("txtInput")

for i in fulltext:
    inputfield.send_keys(i)
    time.sleep(0.01)    #change speed here, the smaller the number, the faster

