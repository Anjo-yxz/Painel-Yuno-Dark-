import secrets
import string
import os
from colorama import Fore, Style

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gsenha(palavra):
    numeros = string.digits
    simbolos = "!@#$%&*+?"
    
    extra1 = secrets.choice(simbolos)
    extra2 = secrets.choice(numeros)
    extra3 = secrets.choice(numeros)
    senha_final = f"{extra1}{palavra.capitalize()}{extra2}{extra3}#"
    return senha_final

INFO = "https://guns.lol/olho_zero"
logo = f"""{Fore.LIGHTMAGENTA_EX}
                ▓██   ██▓ █    ██  ███▄    █  ▒█████       ▀██ ▄█▀ ▓█████▓██   ██▓  ██████ 
                 ▒██  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒      ██▄█▒  ▓█   ▀ ▒██  ██▒▒██    ▒ 
                  ▒██ ██░▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒     ▓███▄░  ▒███    ▒██ ██░░ ▓██▄   
                  ░ ▐██▓░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░     ▓██ █▄  ▒▓█  ▄  ░ ▐██▓░  ▒   ██▒
                  ░ ██▒▓░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░     ▒██▒ █▄▒░▒████  ░ ██▒▓░▒██████▒▒
                   ██▒▒▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░      ▒ ▒▒ ▓▒░░░ ▒░    ██▒▒▒ ▒ ▒▓▒ ▒ ░
                 ▓██ ░▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░      ░ ░▒ ▒░░ ░ ░   ▓██ ░▒░ ░ ░▒  ░ ░
                 ▒ ▒ ░░   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒       ░ ░░ ░     ░   ▒ ▒ ░░  ░  ░  ░  
                 ░ ░        ░              ░     ░ ░       ░  ░   ░   ░   ░ ░           ░ 
                 
                                  {INFO} {Style.RESET_ALL}"""

menu = f"""
{Fore.LIGHTMAGENTA_EX}1 --{Style.RESET_ALL} Gerar key
{Fore.LIGHTMAGENTA_EX}2 --{Style.RESET_ALL} Sair
"""
def acc():
    while True:
        clear()
        print(logo)
        print(menu)
        escolhas = input(f"{Fore.LIGHTMAGENTA_EX}Digita: {Style.RESET_ALL}")
        
        if escolhas == "1":
            clear()
            print(logo)
            u_u = input(f"\n{Fore.LIGHTMAGENTA_EX}Digite sua palavra-chave: {Style.RESET_ALL}")
            resultado = gsenha(u_u)
            print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} Sua senha baseada em '{u_u}': {Fore.LIGHTMAGENTA_EX}{resultado}{Style.RESET_ALL}")
            
        elif escolhas == "2":
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")

        input(f"\nPressione Enter para voltar...")
        clear()

if __name__ == "__main__":
    acc()