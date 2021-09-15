from keyauth import api

import os
import os.path
import platform

keyauthapp = api("your application name", "your owner id", "your application secret","1.0")

with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w") as text_file:
    text_file.write("1.1.1.1 keyauth.com")

print("Initializing")
keyauthapp.init()

print ("""
1.Login
2.Register
3.Upgrade
4.License Key Only
""")
ans=input("Select Option: ") 
if ans=="1": 
    user = input('Provide username: ')
    password = input('Provide password: ')
    keyauthapp.login(user,password)
elif ans=="2":
    user = input('Provide username: ')
    password = input('Provide password: ')
    license = input('Provide License: ')
    keyauthapp.register(user,password,license) 
elif ans=="3":
    user = input('Provide username: ')
    license = input('Provide License: ')
    keyauthapp.upgrade(user,license)
elif ans=="4":
    key = input('Enter your license: ')
    keyauthapp.license(key)
elif ans !="":
  print("\n Not Valid Option") 
