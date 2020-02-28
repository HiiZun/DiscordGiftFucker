# © DiscordGiftFucker - NeiiZun - 28/02/20

import random
import requests
import threading
import time
from colorama import init, Fore
import json
import fake_useragent
import os
from os import system
def checkSystem():
    if os.name == 'nt':
        init(convert=True)
        return 'windows'
    else:
        return 'other'
osname = checkSystem()
def clear():
    if(osname == 'windows'):
        system("cls")
    else:
        system("clear")

def randomString(stringLength):
    letters = "AZERTYUIOPQSDFGHJKLMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbn"
    return ''.join(random.choice(letters) for i in range(stringLength))


def join():
    system("title " + " DISCORD GIFT FUCKER")
    print(Fore.YELLOW + """+---------------------------------------------------------------------------------------+
|                                                                                       |
|     _   _ _ _                      +                                                  |
|    | \ | (_) |                     |  [+] BY NEIIZUN                                  |
|    |  \| |_| |_ _ __ ___           |                                                  |
|    | . ` | | __| '__/ _ \          |  [+] DISCORD: NeiiZun#7916                       |
|    | |\  | | |_| | | (_) |         |                                                  |
|    \_|_\_/_|\__|_| _\___/          |  [+] Don't forget to update your proxies list in |
|    |  ___|        | |              |  'proxies.txt' file                              |
|    | |_ _   _  ___| | _____ _ __   |                                                  |
|    |  _| | | |/ __| |/ / _ \ '__|  |  [+] Made with love <3                           |
|    | | | |_| | (__|   <  __/ |     |                                                  |
|    \_|  \__,_|\___|_|\_\___|_|v2.0 |                                                  |
|                                    |                                                  |
+------------------------------------+                                                  |
|                |--|                |                                                  |
|                |--|                |                                                  |
|                |--|                |                         ((\o/))                  |
|                |--|                |                    .+---+ /^\ +---+.             |
|                |--|                |                    +    /`+ +`\    +             |
|                |--|                |                    |      | |      |             |
|                |--|                |                    |      | |      |             |
|                |--|                |  XX                +      + +      +             |
|XXXXXXX       XXXXXXXX    XXXXXXX   + XXXXXXXXXX    XXXXX'+----+===+----+' XXXXX XXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
+---------------------------------------------------------------------------------------+
""")
    time.sleep(3)

    clear()

    print(Fore.RED + """_____________  _________________________________________
    ___  __/__  / / /__  __ \__  ____/__    |__  __ \_  ___/
    __  /  __  /_/ /__  /_/ /_  __/  __  /| |_  / / /____ \ 
    _  /   _  __  / _  _, _/_  /___  _  ___ |  /_/ /____/ / 
    /_/    /_/ /_/  /_/ |_| /_____/  /_/  |_/_____/ /____/  
                                                            """)
    threads_number = input(Fore.YELLOW + "Enter a number of threads: ")
    threads_number = int(threads_number)


    clear()
    lines = 0
    with open("proxies.txt", "r") as f:
        for line in f:
            lines += 1

    print(Fore.YELLOW + """______ _____ _____ _____ _____ _____ ___________       
|  _  \  ___|_   _|  ___/  __ \_   _|  ___|  _  \      
| | | | |__   | | | |__ | /  \/ | | | |__ | | | |      
| | | |  __|  | | |  __|| |     | | |  __|| | | |      
| |/ /| |___  | | | |___| \__/\ | | | |___| |/ / _ _ _ 
|___/ \____/  \_/ \____/ \____/ \_/ \____/|___(_|_|_|_)
                                                       
                                                       """)
    print(" ")
    print(Fore.YELLOW + "Numbers of proxies: " + Fore.RED + str(lines))
    print(" ")
    print(Fore.YELLOW + "Numbers of threads: " + Fore.RED + str(threads_number))
    time.sleep(3)
    clear()

    print(Fore.RED + """     _____ _____ ___  ______ _____ _____ _   _ _____         
    /  ___|_   _/ _ \ | ___ \_   _|_   _| \ | |  __ \        
    \ `--.  | |/ /_\ \| |_/ / | |   | | |  \| | |  \/        
     `--. \ | ||  _  ||    /  | |   | | | . ` | | __         
    /\__/ / | || | | || |\ \  | |  _| |_| |\  | |_\ \_ _ _ _ 
    \____/  \_/\_| |_/\_| \_| \_/  \___/\_| \_/\____(_|_|_|_)
                                                         
                                                         
    [+] Too slow? check your proxies
    
    """)
    return threads_number

def checker():
    text_file = open("proxies.txt", "r")
    proxieslist = text_file.readlines()
    text_file.close()
    ua = fake_useragent.UserAgent()
    while 1 < 6:
        code = randomString(16)
        ll = random.choice(proxieslist)
        ip = ll.replace('\n', '')
        proxies = {
            'http': 'http://' + ip,
            'https': 'http://' + ip,
        }

        headers = {
            'User-Agent': ua.random,
            'content-type': 'application/json',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

        try:
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true".format(code)
            src = requests.Session().get(url, headers=headers, proxies=proxies, timeout=1)
            resp = json.loads(src.text)
            message = resp["message"].lower()
            if message == "unknown gift code".lower():
                print(Fore.RED + "[MISS] " + "" + code)
            elif message == "you are being rate limited.".lower():
                continue;
            elif message == None:
                print(Fore.BLACK + "[UNKNOW] " + "https://discord.gift/" + code)
                find = open("results/" + "unknow.txt", "a")
                find.write("https://discord.gift/" + code + "\n")
                find.close()
            else:
                print(Fore.GREEN + "[FIND] " + "https://discord.gift/" + code)
                find = open("results/" + "find.txt", "a")
                find.write("https://discord.gift/" + code + "\n")
                find.close()

        except Exception:
            continue;


threads = []

#Start
threads_number = join()

for _ in range(threads_number):
    t = threading.Thread(target=checker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
