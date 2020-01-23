import sys, os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyperclip


#Checks the current directory for 'loginpage.txt' file
#If one is not found, create one and write it generic values of null.
#Then, whether it was there to begin with or not, read the 'loginpage.txt' file.
if 'loginpage.txt' not in os.listdir(os.getcwd()):
    fileRead = open('loginpage.txt', 'w')
    fileRead.write('facebook null null\ntwitter null null')
    fileRead.close()
fileRead = open('loginpage.txt', 'r')


#Creates a new list per line
loginList = fileRead.readlines()
accounts = {}
#print(loginList)

list1 = []

for p in loginList:
    string = p.split()
    #print(string)
    list1 = string[1] + ' ' + string[2]
    #list2 is a list that contains the username/email and password for each account
    #This is so we can store this list as the values in the "accounts" dictionary.
    list2 = list1.split()
    #print(list2)
    accounts[string[0]] = list2
print(accounts)
fileRead.close()

#requires you to pass a dictionary key when running program in cmd.
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

#Needed to utilize google chrome browser.
driver = webdriver.Chrome('chromedriver')

#Function to login to Facebook.
def loginFacebook(username, password):
    #Gets the designated website
    driver.get('https://www.facebook.com/')

    #Find the textfield for the user's email (Crtl + Shift + i to inspect html and find element)
    uname = driver.find_element_by_name('email')
    #Find the textfield for the user's password
    pword = driver.find_element_by_name('pass')
    #Find the button to initiate login.
    loginButton = driver.find_element_by_id('loginbutton')

    #pass values to html elements.
    uname.send_keys(username)
    pword.send_keys(password)
    loginButton.send_keys('Log In')


def loginTwitter(username, password):
    driver.get('https://twitter.com/login')

    uname = driver.find_element_by_css_selector("input[placeholder='Phone, email or username']")
    pword = driver.find_element_by_css_selector("input[class='js-password-field']")
    submit = driver.find_element_by_xpath("//button[text()='Log in']")
    
    uname.send_keys(username)
    pword.send_keys(password)
    submit.click()


key = sys.argv[1]

keysList = list(accounts.keys())
valueList = list(accounts.values())



if key in accounts and len(sys.argv) == 2:
    if key == 'facebook':
        if accounts[key][0] != 'null' and accounts[key][1] != 'null':
            loginFacebook(accounts[key][0], accounts[key][1])
        else:
            driver.close()
            print('Must have a username and password for your facebook account')
            sys.exit()
    elif key == 'twitter':
        if accounts[key][0] != 'null' and accounts[key][1] != 'null':
            loginTwitter(accounts[key][0], accounts[key][1])
        else:
            driver.close()
            print('Must have a username and password for your twitter account')
            sys.exit()

if key in accounts and (sys.argv[2] == 'update' and sys.argv[3] == 'password'):
    driver.close()
    pword = input('Enter new password for ' + key + ' account: ')
    accounts[key][1] = pword
    fileWrite = open('loginpage.txt', 'w')
    for i in range(len(keysList)):
        string = str(keysList[i]) + ' ' + valueList[i][0] + ' ' + valueList[i][1] + '\n'
        fileWrite.write(string)
        i+=1
    fileWrite.close()
    print('Your password hsa been changed')

elif key in accounts and (sys.argv[2] == 'update' and sys.argv[3] == 'username'):
    driver.close()
    uname = input('Enter new username for ' + key + ' account: ')
    accounts[key][0] = uname
    fileWrite = open('loginpage.txt', 'w')
    for i in range(len(keysList)):
        string = str(keysList[i]) + ' ' + valueList[i][0] + ' ' + valueList[i][1] + '\n'
        fileWrite.write(string)
        i+=1
    fileWrite.close()
    print('Your username/email has been changed')
    
    
