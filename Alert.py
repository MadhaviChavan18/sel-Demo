import time

from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
b=Options()
b.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=b)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
'''#for simple alert
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
click1=driver.switch_to.alert
msg=click1.text
print("Alert shows this msg",msg)
click1.accept()
'''
#for confirmation alert
driver.find_element(By.ID,"confirmbtn").click()
time.sleep(2)
click2=driver.switch_to.alert
msg1=click2.text
print("Alert shows this msg",msg1)
time.sleep(2)
click2.dismiss()

time.sleep(2)
driver.refresh()

obj=driver.find_element(By.ID,"confirmbtn")
obj.click()
time.sleep(2)
click2=driver.switch_to.alert
msg1=click2.text
print("Alert shows this msg",msg1)
click2.accept()
