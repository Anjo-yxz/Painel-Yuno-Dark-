import os
import colorama

from colorama import Fore,Style
from function_all import crpy
from function_all import gr_senha
from function_all import varfy_cpf

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def crip():
    clear()
    crpy.acc()

def ger():
    clear()
    gr_senha.acc()

def varfy():
    clear()
    varfy_cpf.acc()

INFO = "https://guns.lol/olho_zero"

logo = f"""{Fore.RED}  
                ▓██   ██▓ █    ██  ███▄    █  ▒█████       ▓█████▄  ▄▄▄      ██▀███   ██ ▄█▀
                 ▒██  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒     ▒██▀ ██▌▒████▄   ▓██ ▒ ██▒ ██▄█▒ 
                  ▒██ ██░▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒     ░██   █▌▒██  ▀█▄ ▓██ ░▄█ ▒▓███▄░ 
                  ░ ▐██▓░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░    ▒░▓█▄   ▌░██▄▄▄▄██▒██▀▀█▄  ▓██ █▄ 
                  ░ ██▒▓░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░    ░░▒████▓ ▒▓█   ▓██░██▓ ▒██▒▒██▒ █▄
                   ██▒▒▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ░ ▒▒▓  ▒ ░▒▒   ▓▒█░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
                 ▓██ ░▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░       ░ ▒  ▒ ░ ░   ▒▒   ░▒ ░ ▒ ░ ░▒ ▒░
                 ▒ ▒ ░░   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒        ░ ░  ░   ░   ▒    ░░   ░ ░ ░░ ░ 
                 ░ ░        ░              ░     ░ ░          ░          ░     ░     ░  ░   
                 
                                    {INFO}
                 {Style.RESET_ALL}
"""

menu = f"""{Fore.RED}
┌─ Creator: Olho_zero  ┐
├─ Yuno Dark           │
└──────────────────────┘
┌─ [+] 1 - Criptografar
│
├─ [+] 2 - Valid Cpf
│
├─ [+] 3 - Gerar Senha Forte
│
└─ [+] 4 - Sair
{Style.RESET_ALL}
"""

while True:
    clear()
    print(logo)
    print(menu)
    escolhas = input(f"Digita:{Fore.RED} ")
    print(Style.RESET_ALL, end="")
    if escolhas == "1":
        clear()
        crip()
    elif escolhas == "2":
        clear()
        varfy()
    elif escolhas == "3":
        clear()
        ger()
    elif escolhas == "4":
        clear()
        break

    input("...")
    clear()