from pynput.keyboard import Key, Controller
import time
import threading
import json
from colorama import Fore, Back
import os
import requests
import webbrowser
active = False
timeSincewalked = 0
keyboard = Controller()
def presskey(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)

def go_to_council():
        presskey('d', 1.52)
        presskey('w', 2.61)
        presskey('d', 11.39)
        presskey('s', 1.0)
        presskey('d', 1.23)
        presskey('s', 3.46)
        presskey('d', 0.96)
        presskey('w', 3.81)
        presskey('d', 0.79)
        presskey('s', 0.6)
        presskey('d', 2.04)
        presskey('s', 0.1)
print('Grg Farm 1.0')
time.sleep(1)
print('Made by _Sleepy')
print(Fore.RED + "This might get you banned in generic roleplay gaem. I am not responsible for any damages that happen using this tool." + Fore.RESET)
priv = input('Private Server Link: ')
print("Connecting to Roblox")
start = time.time()
response = requests.get("https://www.roblox.com/home")
timetaken = round((time.time() - start) * 1000)
print("Connected to Roblox, Estimated ping: {0}ms".format(timetaken))
print("Don't touch anything unless you want to cancel/stop. We are going to open Roblox and to everything for you.")
time.sleep(5)
webbrowser.open(priv)
time.sleep(300)
go_to_council()
def pressE():
    while active == True:
        presskey('e', 10)
        time.sleep(60)
active = True
def count():
    while True:
        global timeSincewalked
        timeSincewalked += 1
        time.sleep(1)
        if timeSincewalked >= 1000:
            go_to_council()
            timeSincewalked = 0
x = threading.Thread(target=pressE)
z = threading.Thread(target=count)
x.start()
z.start()
