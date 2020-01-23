from tkinter import *
from tkinter import messagebox
import sys, os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Application(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.readFile()
        #self.create_widgets.()




    def create_widgets(self):

        frame19 = Frame()
        frame19.config(width=150)
        frame19['bg'] = '#2D365D'
        frame19.pack(pady=30)


        frame18 = Frame(frame19)
        frame18.pack()

        frame1 = Frame(frame19)
        frame1.pack()
        frame1['bg'] = '#2D365D'


#5F5F5F
        self.lbl = Label(frame18, text="AutoLogin")
        self.lbl['bg'] = '#2D365D'
        self.lbl.config(font=('Courier', 28), fg='#FE2A00')
        self.lbl.pack()

        self.bttnFacebook = Button(frame1, text = "Facebook")
        self.bttnFacebook.config(font=('Courier', 10), background='#5F5F5F', fg='white')
        self.bttnFacebook["command"]=self.bttn_click_facebook
        self.bttnFacebook.pack(padx=5, pady=10, side=LEFT)

        self.bttnTwitter = Button(frame1, text = "Twitter")
        self.bttnTwitter.config(font=('Courier', 10), background='#5F5F5F', fg='white')
        self.bttnTwitter["command"]=self.bttn_click_twitter
        self.bttnTwitter.pack(padx=5, pady=10, side=LEFT)

        self.bttnTwitch = Button(frame1, text = "Twitch")
        self.bttnTwitch.config(font=('Courier', 10), background='#5F5F5F', fg='white')
        self.bttnTwitch["command"]=self.bttn_click_twitch
        self.bttnTwitch.pack(padx=5, pady=10, side=LEFT)

        frame2 = Frame()
        frame2.pack()
        self.lblUpdateAccount = Label(frame2, text="Update Account Info in Text File")
        self.lblUpdateAccount['bg'] = '#2D365D'
        self.lblUpdateAccount.config(font=('Courier', 13), fg='#FE2A00')
        self.lblUpdateAccount.pack()



        frame8 = Frame()
        frame8['bg'] = '#2D365D'
        frame8.pack()



        frame3 = Frame(frame8)
        frame3['bg'] = '#2D365D'
        frame3.pack(padx=5, pady=10, side=LEFT)

        frame4 = Frame(frame3)
        frame4['bg'] = '#2D365D'
        self.lblFacebook = Label(frame4, text="Facebook")
        self.lblFacebook['bg'] = '#2D365D'
        self.lblFacebook.config(font=('Courier', 12), fg='white')
        self.lblFacebook.pack()
        frame4.pack(padx=5, pady=10, side=LEFT)

        frame5 = Frame(frame3)
        frame5['bg'] = '#2D365D'
        self.lblfbAccount = Label(frame5, text="account")
        self.lblfbAccount['bg'] = '#2D365D'
        self.lblfbAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblfbAccount.pack(padx=5, pady=6, side=LEFT)

        self.entryFbAccount = Entry(frame5)
        self.entryFbAccount.config(font=('Courier', 10))
        self.entryFbAccount.pack(padx=2, pady=6, side=LEFT)

        self.bttnUpdateFbAccount = Button(frame5, text="update")
        self.bttnUpdateFbAccount['bg'] = '#5F5F5F'
        self.bttnUpdateFbAccount.config(font=('Courier', 10), fg='white')
        self.bttnUpdateFbAccount["command"]=self.update_facebookAccount
        self.bttnUpdateFbAccount.pack(padx=2, pady=6, side=LEFT)
        frame5.pack()

        frame6 = Frame(frame3)
        frame6['bg'] = '#2D365D'
        self.lblfbPassword = Label(frame6, text="password")
        self.lblfbPassword['bg'] = '#2D365D'
        self.lblfbPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblfbPassword.pack(padx=5, pady=10, side=LEFT)

        self.entryFbPassword = Entry(frame6)
        self.entryFbPassword.config(font=('Courier', 10), show="*")
        self.entryFbPassword.pack(padx=2, pady=10, side=LEFT)

        self.bttnUpdateFbPassword = Button(frame6, text="update")
        self.bttnUpdateFbPassword['bg'] = '#5F5F5F'
        self.bttnUpdateFbPassword.config(font=('Courier', 10), fg='white')
        self.bttnUpdateFbPassword["command"]=self.update_facebookPassword
        self.bttnUpdateFbPassword.pack(padx=2, pady=6, side=LEFT)
        frame6.pack()




        frame9 = Frame(frame8)
        frame9['bg'] = '#2D365D'
        frame9.pack(padx=12, pady=10, side=LEFT)


        frame10 = Frame(frame9)
        frame10['bg'] = '#2D365D'
        self.lblTwitter = Label(frame10, text="Twitter")
        self.lblTwitter['bg'] = '#2D365D'
        self.lblTwitter.config(font=('Courier', 12), fg='white')
        self.lblTwitter.pack()
        frame10.pack(padx=5, pady=10, side=LEFT)

        frame11 = Frame(frame9)
        frame11['bg'] = '#2D365D'
        self.lblTwitterAccount = Label(frame11, text="account")
        self.lblTwitterAccount['bg'] = '#2D365D'
        self.lblTwitterAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitterAccount.pack(padx=5, pady=6, side=LEFT)

        self.entryTwitterAccount = Entry(frame11)
        self.entryTwitterAccount.config(font=('Courier', 10))
        self.entryTwitterAccount.pack(padx=2, pady=6, side=LEFT)

        self.bttnUpdateTwitterAccount = Button(frame11, text="update")
        self.bttnUpdateTwitterAccount['bg'] = '#5F5F5F'
        self.bttnUpdateTwitterAccount.config(font=('Courier', 10), fg='white')
        self.bttnUpdateTwitterAccount["command"]=self.update_twitterAccount
        self.bttnUpdateTwitterAccount.pack(padx=2, pady=6, side=LEFT)
        frame11.pack()

        frame12 = Frame(frame9)
        frame12['bg'] = '#2D365D'
        self.lblTwitterPassword = Label(frame12, text="password")
        self.lblTwitterPassword['bg'] = '#2D365D'
        self.lblTwitterPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitterPassword.pack(padx=5, pady=10, side=LEFT)

        self.entryTwitterPassword = Entry(frame12)
        self.entryTwitterPassword.config(font=('Courier', 10), show="*")
        self.entryTwitterPassword.pack(padx=2, pady=10, side=LEFT)

        self.bttnUpdateTwitterPassword = Button(frame12, text="update")
        self.bttnUpdateTwitterPassword['bg'] = '#5F5F5F'
        self.bttnUpdateTwitterPassword.config(font=('Courier', 10), fg='white')
        self.bttnUpdateTwitterPassword["command"]=self.update_twitterPassword
        self.bttnUpdateTwitterPassword.pack(padx=2, pady=6, side=LEFT)
        frame12.pack()




        frame13 = Frame(frame8)
        frame13['bg'] = '#2D365D'
        frame13.pack(padx=5, pady=10, side=LEFT)


        frame14 = Frame(frame13)
        frame14['bg'] = '#2D365D'
        self.lblTwitch = Label(frame14, text="Twitch")
        self.lblTwitch['bg'] = '#2D365D'
        self.lblTwitch.config(font=('Courier', 12), fg='white')
        self.lblTwitch.pack()
        frame14.pack(padx=5, pady=10, side=LEFT)

        frame15 = Frame(frame13)
        frame15['bg'] = '#2D365D'
        self.lblTwitchAccount = Label(frame15, text="account")
        self.lblTwitchAccount['bg'] = '#2D365D'
        self.lblTwitchAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitchAccount.pack(padx=5, pady=6, side=LEFT)

        self.entryTwitchAccount = Entry(frame15)
        self.entryTwitchAccount.config(font=('Courier', 10))
        self.entryTwitchAccount.pack(padx=2, pady=6, side=LEFT)

        self.bttnUpdateTwitchAccount = Button(frame15, text="update")
        self.bttnUpdateTwitchAccount['bg'] = '#5F5F5F'
        self.bttnUpdateTwitchAccount.config(font=('Courier', 10), fg='white')
        self.bttnUpdateTwitchAccount["command"]=self.update_twitchAccount
        self.bttnUpdateTwitchAccount.pack(padx=2, pady=6, side=LEFT)
        frame15.pack()

        frame16 = Frame(frame13)
        frame16['bg'] = '#2D365D'
        self.lblTwitchPassword = Label(frame16, text="password")
        self.lblTwitchPassword['bg'] = '#2D365D'
        self.lblTwitchPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitchPassword.pack(padx=5, pady=10, side=LEFT)

        self.entryTwitchPassword = Entry(frame16)
        self.entryTwitchPassword.config(font=('Courier', 10), show="*")
        self.entryTwitchPassword.pack(padx=2, pady=10, side=LEFT)

        self.bttnUpdateTwitchPassword = Button(frame16, text="update")
        self.bttnUpdateTwitchPassword['bg'] = '#5F5F5F'
        self.bttnUpdateTwitchPassword.config(font=('Courier', 10), fg='white')
        self.bttnUpdateTwitchPassword["command"]=self.update_twitchPassword
        self.bttnUpdateTwitchPassword.pack(padx=2, pady=6, side=LEFT)
        frame16.pack()



    #New window for if the text file does not exist in the current directory.
    def create_widgets1(self):
        global frame2
        frame2 = Frame()
        frame2.pack()
        self.lblUpdateAccount = Label(frame2, text="Save account information in text file.")
        self.lblUpdateAccount['bg'] = '#2D365D'
        self.lblUpdateAccount.config(font=('Courier', 13), fg='white')
        self.lblUpdateAccount.pack()


        global frame8
        frame8 = Frame()
        frame8['bg'] = '#2D365D'
        frame8.pack()



        frame3 = Frame(frame8)
        frame3['bg'] = '#2D365D'
        frame3.pack(padx=5, pady=10, side=LEFT)

        frame4 = Frame(frame3)
        frame4['bg'] = '#2D365D'
        self.lblFacebook = Label(frame4, text="Facebook")
        self.lblFacebook['bg'] = '#2D365D'
        self.lblFacebook.config(font=('Courier', 12), fg='white')
        self.lblFacebook.pack()
        frame4.pack(padx=5, pady=10, side=LEFT)

        frame5 = Frame(frame3)
        frame5['bg'] = '#2D365D'
        self.lblfbAccount = Label(frame5, text="account")
        self.lblfbAccount['bg'] = '#2D365D'
        self.lblfbAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblfbAccount.pack(padx=5, pady=6, side=LEFT)
        
        self.entryFbAccount = Entry(frame5)
        self.entryFbAccount.config(font=('Courier', 10))
        self.entryFbAccount.pack(padx=2, pady=6, side=LEFT)
        frame5.pack()

        frame6 = Frame(frame3)
        frame6['bg'] = '#2D365D'
        self.lblfbPassword = Label(frame6, text="password")
        self.lblfbPassword['bg'] = '#2D365D'
        self.lblfbPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblfbPassword.pack(padx=5, pady=10, side=LEFT)
        
        self.entryFbPassword = Entry(frame6)
        self.entryFbPassword.config(font=('Courier', 10), show="*")
        self.entryFbPassword.pack(padx=2, pady=10, side=LEFT)
        frame6.pack()




        frame9 = Frame(frame8)
        frame9['bg'] = '#2D365D'
        frame9.pack(padx=12, pady=10, side=LEFT)


        frame10 = Frame(frame9)
        frame10['bg'] = '#2D365D'
        self.lblTwitter = Label(frame10, text="Twitter")
        self.lblTwitter['bg'] = '#2D365D'
        self.lblTwitter.config(font=('Courier', 12), fg='white')
        self.lblTwitter.pack()
        frame10.pack(padx=5, pady=10, side=LEFT)

        frame11 = Frame(frame9)
        frame11['bg'] = '#2D365D'
        self.lblTwitterAccount = Label(frame11, text="account")
        self.lblTwitterAccount['bg'] = '#2D365D'
        self.lblTwitterAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitterAccount.pack(padx=5, pady=6, side=LEFT)
        
        self.entryTwitterAccount = Entry(frame11)
        self.entryTwitterAccount.config(font=('Courier', 10))
        self.entryTwitterAccount.pack(padx=2, pady=6, side=LEFT)
        frame11.pack()

        frame12 = Frame(frame9)
        frame12['bg'] = '#2D365D'
        self.lblTwitterPassword = Label(frame12, text="password")
        self.lblTwitterPassword['bg'] = '#2D365D'
        self.lblTwitterPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitterPassword.pack(padx=5, pady=10, side=LEFT)
        
        self.entryTwitterPassword = Entry(frame12)
        self.entryTwitterPassword.config(font=('Courier', 10), show="*")
        self.entryTwitterPassword.pack(padx=2, pady=10, side=LEFT)
        frame12.pack()




        frame13 = Frame(frame8)
        frame13['bg'] = '#2D365D'
        frame13.pack(padx=5, pady=10, side=LEFT)


        frame14 = Frame(frame13)
        frame14['bg'] = '#2D365D'
        self.lblTwitch = Label(frame14, text="Twitch")
        self.lblTwitch['bg'] = '#2D365D'
        self.lblTwitch.config(font=('Courier', 12), fg='white')
        self.lblTwitch.pack()
        frame14.pack(padx=5, pady=10, side=LEFT)

        frame15 = Frame(frame13)
        frame15['bg'] = '#2D365D'
        self.lblTwitchAccount = Label(frame15, text="account")
        self.lblTwitchAccount['bg'] = '#2D365D'
        self.lblTwitchAccount.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitchAccount.pack(padx=5, pady=6, side=LEFT)
        
        self.entryTwitchAccount = Entry(frame15)
        self.entryTwitchAccount.config(font=('Courier', 10))
        self.entryTwitchAccount.pack(padx=2, pady=6, side=LEFT)
        frame15.pack()

        frame16 = Frame(frame13)
        frame16['bg'] = '#2D365D'
        self.lblTwitchPassword = Label(frame16, text="password")
        self.lblTwitchPassword['bg'] = '#2D365D'
        self.lblTwitchPassword.config(font=('Courier', 10), fg='#FE2A00')
        self.lblTwitchPassword.pack(padx=5, pady=10, side=LEFT)
        
        self.entryTwitchPassword = Entry(frame16)
        self.entryTwitchPassword.config(font=('Courier', 10), show="*")
        self.entryTwitchPassword.pack(padx=2, pady=10, side=LEFT)
        frame16.pack()

        global frame17
        frame17 = Frame()
        frame17['bg'] = '#2D365D'

        self.bttnSubmit = Button(frame17, text="Submit")
        self.bttnSubmit['bg'] = '#5F5F5F'
        self.bttnSubmit.config(font=('Courier', 10), fg='white')
        self.bttnSubmit["command"]=self.bttn_submit
        #self.bttnSubmit["command"]=frame8.pack_forget()
        self.bttnSubmit.pack()
        frame17.pack()





    def readFile(self):
        #Checks to see if the text file is in the current directory.
        if 'loginpage.txt' not in os.listdir(os.getcwd()):
            self.create_widgets1()
            fileWrite = open('loginpage.txt', 'w')
            fileWrite.write('facebook null null\ntwitter null null\ntwitch null null')
            fileWrite.close()
        else:
            self.create_widgets()

        fileRead = open('loginpage.txt', 'r')

        #Creates a new list per line
        loginList = fileRead.readlines()

        #Declares and instantiates 'accounts' dictionary.
        global accounts
        accounts = {}
        #print(loginList)

        #Declares 'list1' list.
        list1 = []

        for p in loginList:
            string = p.split()
            #print(string)

            '''list 1 is a list containing the second(username/email) and the third(password) values
               of each line'''
            list1 = string[1] + ' ' + string[2]
            #list2 is a list that contains the username/email and password for each account
            #It splits list1 at the space so the values are stored individually.
            #This is so we can store this list as the values in the "accounts" dictionary.
            list2 = list1.split()
            #print(list2)

            '''this sets each key in the 'accounts' dictionary to the first element in
               in the 'string' list and each value equal to 'list2'.'''
            accounts[string[0]] = list2
            
        print(accounts)
        fileRead.close()
        global keysList
        keysList = list(accounts.keys())
        global valuesList
        valuesList = list(accounts.values())
        #print(keysList)



    def bttn_submit(self):
        '''If the entry does not equal an empty string, then set the first value of the
        'facebook' dictionary to the entry. If it does equal an empty string, then don't do anything
        to it which will leave the value as 'null'.'''
        if self.entryFbAccount.get() != '':
            accounts['facebook'][0] = self.entryFbAccount.get()
        if self.entryFbPassword.get() != '':
            accounts['facebook'][1] = self.entryFbPassword.get()

        if self.entryTwitterAccount.get() != '':
            accounts['twitter'][0] = self.entryTwitterAccount.get()
        if self.entryTwitterPassword.get() != '':
            accounts['twitter'][1] = self.entryTwitterPassword.get()

        if self.entryTwitchAccount.get() != '':
            accounts['twitch'][0] = self.entryTwitchAccount.get()
        if self.entryTwitchPassword.get() != '':
            accounts['twitch'][1] = self.entryTwitchPassword.get()

        fileWrite = open('loginpage.txt', 'w')
        for i in range(len(keysList)):
            string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
            fileWrite.write(string)
            i+=1
        fileWrite.close()
        messagebox.showinfo("Success!", "Update Successful")
        frame2.pack_forget()
        frame8.pack_forget()
        frame17.pack_forget()
        self.create_widgets()



    #Function to login to Facebook.
    def loginFacebook(self, username, password):
        driver = webdriver.Chrome('chromedriver')
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


    def loginTwitter(self, username, password):
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://twitter.com/login')

        uname = driver.find_element_by_css_selector("input[placeholder='Phone, email or username']")
        pword = driver.find_element_by_css_selector("input[class='js-password-field']")
        submit = driver.find_element_by_xpath("//button[text()='Log in']")

        uname.send_keys(username)
        pword.send_keys(password)
        submit.click()

    def loginTwitch(self, username, password):
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://www.twitch.tv/')

        login = driver.find_element_by_xpath("//button[@data-a-target='login-button']")
        login.click()
        time.sleep(2)
        uname = driver.find_element_by_xpath("//div[@class='tw-relative']/input[@type='text']")

        pword = driver.find_element_by_css_selector("input[type='password']")

        uname.send_keys(username)
        pword.send_keys(password)

        passportLogin = driver.find_element_by_xpath("//button[@data-a-target='passport-login-button']")
        passportLogin.click()



    def bttn_click_facebook(self):
        '''Passes the username and password from the dictionary named 'accounts'
           where the key = 'facebook' and the username is the first element of the value
           and the password is the second element of the value (each value is a list).'''
        self.loginFacebook(accounts['facebook'][0], accounts['facebook'][1])
        print(accounts)


    def bttn_click_twitter(self):
        self.loginTwitter(accounts['twitter'][0], accounts['twitter'][1])
        print(accounts)


    def bttn_click_twitch(self):
        self.loginTwitch(accounts['twitch'][0], accounts['twitch'][1])
        print(accounts)


    #Function that updates facebook username/email in the text file.
    #Use similar functions to update username/email and passwords for the rest of the accounts
    def update_facebookAccount (self):
        #sets the text in "self.entryFbAccount" to the variable "contents"
        contents = self.entryFbAccount.get()

        #checks that the entry field is not empty
        if contents != '':
            #Assigns the first value in the list of values assigned to the key 'facebook' to
            #the contents of the corresponding entry field.
            accounts['facebook'][0] = contents
            fileWrite = open('loginpage.txt', 'w')
            #Loop that re-writes the entire text file.
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            #clears the entry field.
            self.entryFbAccount.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




    def update_facebookPassword (self):
        contents = self.entryFbPassword.get()

        if contents != '':
            accounts['facebook'][1] = contents
            fileWrite = open('loginpage.txt', 'w')
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            self.entryFbPassword.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




    def update_twitterAccount (self):
        contents = self.entryTwitterAccount.get()

        if contents != '':
            accounts['twitter'][0] = contents
            fileWrite = open('loginpage.txt', 'w')
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            self.entryTwitterAccount.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




    def update_twitterPassword (self):
        contents = self.entryTwitterPassword.get()

        if contents != '':
            accounts['twitter'][1] = contents
            fileWrite = open('loginpage.txt', 'w')
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            self.entryTwitterPassword.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




    def update_twitchAccount (self):
        contents = self.entryTwitchAccount.get()

        if contents != '':
            accounts['twitch'][0] = contents
            fileWrite = open('loginpage.txt', 'w')
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            self.entryTwitchAccount.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




    def update_twitchPassword (self):
        contents = self.entryTwitchPassword.get()

        if contents != '':
            accounts['twitch'][1] = contents
            fileWrite = open('loginpage.txt', 'w')
            for i in range(len(keysList)):
                string = str(keysList[i]) + ' ' + valuesList[i][0] + ' ' + valuesList[i][1] + '\n'
                fileWrite.write(string)
                i+=1
            fileWrite.close()
            print('account updated')
            messagebox.showinfo("Success!", "Update Successful")
            self.entryTwitchPassword.delete(0, END)
        else:
            messagebox.showerror("Error", "You must enter a value")
        self.entryFbAccount.delete(0, END)




#main
root = Tk()
root['bg'] = "#2D365D"
root.title("AutoLogin V4")
root.geometry("1300x285")
root.resizable(width = False, height = True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

app = Application(root)
root.mainloop()
