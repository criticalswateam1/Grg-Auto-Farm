import time
import threading
import requests
import webbrowser
from pynput.keyboard import Key, Controller
from colorama import Fore, Style, init
from urllib.parse import urlparse
from pystyle import Write, System, Colors, Colorate
# Initialize variables
active = False
time_since_walked = 0
keyboard = Controller()

# Function to simulate key press
def press_key(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)

# Function to navigate to council
def go_to_council():
    press_key('d', 1.52)
    press_key('w', 2.61)
    press_key('d', 11.39)
    press_key('s', 1.0)
    press_key('d', 1.23)
    press_key('s', 3.46)
    press_key('d', 0.96)
    press_key('w', 3.81)
    press_key('d', 0.79)
    press_key('s', 0.6)
    press_key('d', 2.04)
    press_key('s', 0.1)

# Function to press 'e' key
def press_e():
    while active:
        press_key('e', 10)
        time.sleep(60)

# Function to count time since walked
def count():
    global time_since_walked
    while True:
        time_since_walked += 1
        time.sleep(1)
        if time_since_walked >= 1000:
            go_to_council()
            time_since_walked = 0

# Main function
def bcolors():
    return {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKCYAN': '\033[96m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }
def main():
    colors = bcolors()
    time.sleep(1)
    print(f"{Fore.MAGENTA}[!] This version is the offical version of Generic Roleplay Autofarm. For more information please contact (_sovietcat.).")
    print(f"{Fore.MAGENTA}If you encounter any issues, please open a Github issue and our staff team will get back to you as soon as possible.")
    print(f"{Fore.MAGENTA}Github : github.com/SleepyHeres/Grg-Auto-Farm/tree/1.0.0")
    print(f"{Fore.MAGENTA}[!] This piece of code is a pull request submitted by criticaldevx.")
    print(f"{colors['WARNING']}Warning: Using this tool could get you banned in Generic Roleplay Game. Enter the private server link to continue.{colors['ENDC']}")
    priv = input(f"{colors['OKCYAN']}root@grgfarm{colors['ENDC']} {colors['OKBLUE']}~> Private Server Link:{colors['ENDC']} ")
    print(f"{colors['FAIL']}Initiating connection to Roblox Servers.{colors['FAIL']}")
    start = time.time()
    response = requests.get("https://www.roblox.com/home")
    time_taken = round((time.time() - start) * 1000)
    print(f"{colors['OKGREEN']}[!] Connected to Roblox Servers! Estimated ping: {time_taken}ms{colors['OKGREEN']}")
    print(f"{colors['WARNING']}Please refrain from any interaction unless you intend to halt the bot. We are in the process of launching Roblox and handling all operations.{colors['ENDC']}")
    time.sleep(5)
    webbrowser.open(priv)
    time.sleep(300)
    go_to_council()
    global active
    active = True
    x = threading.Thread(target=press_e)
    z = threading.Thread(target=count)
    x.start()
    z.start()

if __name__ == "__main__":
    main()
