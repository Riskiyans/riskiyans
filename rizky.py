import os
import sys
import time
import random






os.system('clear')
wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan





def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():

    runntxt(GL+"               __ _     _    _                          ")
    runntxt(GL+"              /__(_)___| | _(_)  _   _  __ _ _ __  ___  ")
    runntxt(WW+"             / \// / __| |/ / | | | | |/ _` | '_ \/ __| ")
    runntxt(WW+"            / _  \ \__ \   <| | | |_| | (_| | | | \__ \ ")
    runntxt(GL+"            \/ \_/_|___/_|\_\_|  \__, |\__,_|_| |_|___/ ")
    runntxt(WW+"                                 |___/                  ")

    runntxt(Y+"       [+]===================================================[+]")
    runntxt(GG+"                      SELAMAT DATANG DI TOOLS SAYA")
    runntxt(Y+"       [+]===================================================[+]")
    runntxt(Y+"")
    runntxt(Y+"")
banner()



print(WW+'[1]','\033[36;1m. DARKFB V1.4')
print(GL+"==============================")
print(WW+'[2]','\033[36;1m. DARKFB V1.6 ')
print(GL+'==============================')
print(WW+'[3]','\033[36;1m. DARK-IG ')
print(GL+'==============================')
print(WW+'[4]','\033[36;1m. SPAM CALL')
print(GL+'==============================')
print(GL+"")
print(GL+"")
print(WW+'[0]','\033[31m. EXIT')
print(WW+'==============================')


def main():
     pilihan = input(YY+'╰──────=>>[PILIH NOMORNYA] :')
     if pilihan == '1' or pilihan == '01':
      print ('EXSPLOITING..........V1.4')
      os.system('pkg install python2')
      os.system('python2 dark.py')
     if pilihan == '2' or pilihan == '02':
      print ('EXSPLOITING..........v1.6')
      os.system('pkg install python2')
      os.system('pip2 install mechanize')
      os.system('pip2 install requests')
      os.system('python2 run.py')
     if pilihan == '3' or pilihan == '03':
      os.system('pkg install python2')
      os.system('pip2 install requests')
      os.system('pip2 install bs4')
      os.system('python2 sc.py')
     if pilihan == '4' or pilihan == '04':
      os.system('pkg install python2')
      os.system('pkg install php')
      os.system('php call.php')







main()
