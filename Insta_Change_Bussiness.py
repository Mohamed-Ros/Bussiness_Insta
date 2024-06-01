#--------------------------------------------------------

#ScriptName : Insta_Bussiness.py

#Switch to professional account

#--------------------------------------------------------



#Script libraries
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
 
from selenium.webdriver.support.select import Select
import os

#--------------------------------------------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKGREEN +""" 

 /$$$$$$$   /$$$$$$   /$$$$$$       /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$      /$$
| $$__  $$ /$$__  $$ /$$__  $$     |__  $$__/| $$_____/ /$$__  $$| $$$    /$$$
| $$  \ $$| $$  \ $$| $$  \__/        | $$   | $$      | $$  \ $$| $$$$  /$$$$
| $$$$$$$/| $$  | $$|  $$$$$$  /$$$$$$| $$   | $$$$$   | $$$$$$$$| $$ $$/$$ $$
| $$__  $$| $$  | $$ \____  $$|______/| $$   | $$__/   | $$__  $$| $$  $$$| $$
| $$  \ $$| $$  | $$ /$$  \ $$        | $$   | $$      | $$  | $$| $$\  $ | $$
| $$  | $$|  $$$$$$/|  $$$$$$/        | $$   | $$$$$$$$| $$  | $$| $$ \/  | $$
|__/  |__/ \______/  \______/         |__/   |________/|__/  |__/|__/     |__/
                                                                              
                 (( FOR CONTACT DEVLOPER ))
                  TELEGRAM : @ROS_TEAM                                                           
                                                                              
"""+ bcolors.HEADER)
#-----------------------------------------------------

time.sleep(3)
take = input("Enter File Name Accounts Want To Change It :")
Acc = open(take,"r").read().splitlines()
count = 0
for C in Acc:
    count += 1
print(f"[=] Accounts Loded [ {count} ]")   
#get_info  
for Accounts in Acc:

  x_user = Accounts.split(':')[0]
  x_passw = Accounts.split(':')[1]
#--------------------------------------------------------

#BROWSER
  driver= webdriver.geckodriver()
  url = ('https://www.instagram.com/accounts/convert_to_professional_account/')

  driver.get(url)

 # driver.maximize_window()

  time.sleep(30)

#--------------------------------------------------------

#COD-LOGIN

  user = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(x_user)

  time.sleep(2)

  paass = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(x_passw) 

  time.sleep(2)

  log = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
  time.sleep(7)

#--------------------------------------------------------

#SAVE-INFO

  save = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
  time.sleep(7)

#--------------------------------------------------------     


#STEP-Switch to professional account 
  box = driver.find_element(By.ID, 'igCoreRadioButtonaccount_typebusiness').click()
  time.sleep(5)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(6)
  ne_xt = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div[2]/div/div[2]/button').click()
  time.sleep(7)
  ne_xt2 = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div[2]/div/div[2]/button').click()
  time.sleep(5)
  category = driver.find_element(By.XPATH, '//*[@id="igCoreRadioButtoncategory2214"]').click()
  time.sleep(5)
  Done = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div[2]/div/div[2]/button').click()
  time.sleep(15)
  Donet = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div[2]/div/div[1]/button').click()
  time.sleep(10)
  finish_Done = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/div[2]/div/div[2]/button').click()
  time.sleep(5)

#--------------------------------------------------------   


#close-Browser
  driver.close()


#TEAM-ROS
#--------------------------------------------------------
  print("[+] Done By ROS :" + x_user )

  myFile = open('save.txt','a')
  myFile.write( " : user done : "'\n' + x_user)
  myFile.close()

