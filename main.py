from os import system

try:
    system("pip install colorama && pip install pyfiglet")
except:pass

from colorama import Fore as f 
from pyfiglet import figlet_format
from time import sleep
from random import choice

system("cls")
sleep(1)

b = figlet_format(text="h s l", font="isometric1")+"\n"+"\n"
print(f.YELLOW, b)


x = input(f"{f.LIGHTCYAN_EX}Please Enter For Start ... ")

if x == "":
    print("")
    print("")
    print("")
    sleep(1)
    code = ["http://3.1.4.3/f//i////l////1.2.4.5.6.7.6.3.2.2.(Rubika).8.3.6.2.(RaKs).fil.ter.3.4.1.9(mrs.haiger).2.4.1.8.6/4.2.4.8/f////g.h/4.2.4.6.4.7.8.4.6.5.8.2.3.7.6.0.3.6.2(http://ffmodmenu.page.link/Anti-V)https://s4.uupload.ir/files/images_(2)_32w.jpeg(*https://bit.ly/3ild93L*)http://kasrahacker.blogside.ir/https://darkweb24.net/?s=https%3A%2F%2Frubika.ir%2Fkasrahacker(http://4.0.1.4/f.i.h/gk/4.5.3//5.2.5.7.2.6.8.4.2.4.7.9.3.1.5.2.7.9.8.0.1.3"]
    print(f.GREEN, choice(code))
    print("")
    print("")
    print("")
else:
    exit()
