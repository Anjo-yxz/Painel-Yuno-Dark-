import os
import validate_docbr
import time
import colorama
import requests
from validate_docbr import CPF
from discord_webhook import DiscordWebhook
from colorama import Fore,Style


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def verfy():
    ferramenta = CPF()
    valida = input("Informe o cpf: ")
    print(f"{Fore.LIGHTMAGENTA_EX}[+] Certo Yuno Validanto{Style.RESET_ALL}")
    time.sleep(5)
    if valida and ferramenta.validate(valida):
        clear()
        print(f"{Fore.LIGHTMAGENTA_EX}CPF Valido {valida}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] Invalido Yuno{Style.RESET_ALL}")

def generator():
    try:
        esolhas = int(input(f"{Fore.LIGHTMAGENTA_EX}Yuno --- Quer gerar quandos ? {Style.RESET_ALL}\nDigitar: "))
        clear()
        ferramenta = CPF()
        salve = []
        for _ in range(esolhas):
            gerar = ferramenta.generate()
            informa = ferramenta.mask(gerar)
            salve.append(informa)
            print(informa)
    except ValueError:
        print("O numero Tem que ser Inteiro")

    try:
        print(f"{Fore.LIGHTMAGENTA_EX}Quer envia em webhook para o Discord ? s/n{Style.RESET_ALL}")
        esolhas1 = input("Digita: ").lower()
        clear()
        if esolhas1 in ["s","sim"]:
            web = input("Webhook: ")
            web_url = DiscordWebhook(web)
            web_url.content = "\n".join(salve)
            web_url.execute()
            print("[+] Salvo com sucesso Yuno :3")
        elif esolhas1 in ["n","não"]:
            print("[=] ok")
    except Exception as e:
            print(f"{Fore.RED}[!] Erro crítico ao enviar Webhook: {e}{Style.RESET_ALL}")

def kitty_hello():
    headers = {'User-Agent': 'curl/7.68.0'}
    url = "https://ascii.live/kitty"

    reqs = requests.get(url,headers=headers,stream=True)
    cont = 0
    contt = 10000
    for n in reqs.iter_lines():
        if n:
            print(Fore.LIGHTMAGENTA_EX, n.decode('utf-8'))
            cont += 1
            if cont > contt:
                 Style.RESET_ALL
                 break

INFO = "https://guns.lol/olho_zero"

logo = f"""{Fore.LIGHTMAGENTA_EX}  
                    ▓██   ██▓ █    ██  ███▄    █  ▒█████       ▄████▄  ██▓███     █████
                     ▒██  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒    ▒██▀ ▀█ ▓██░  ██  ▓██    
                      ▒██ ██░▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒    ▒▓█    ▄▓██░ ██▓▒ ▒████  
                      ░ ▐██▓░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░    ▒▓▓▄ ▄██▒██▄█▓▒ ▒ ░▓█▒   
                      ░ ██▒▓░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░    ▒ ▓███▀ ▒██▒ ░  ░▒░▒█░   
                       ██▒▒▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ░ ░▒ ▒  ▒▓▒░ ░  ░░ ▒ ░   
                     ▓██ ░▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░       ░  ▒  ░▒ ░     ░ ░     
                     ▒ ▒ ░░   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒      ░       ░░         ░ ░   
                     ░ ░        ░              ░     ░ ░      ░ ░              ░       

                                        {INFO}

{Style.RESET_ALL}
"""
menu = f"""{Fore.MAGENTA}  
1 -- Verfy Cpf
2 -- Create Cpf
3 -- Kitty
4 -- Sair
{Style.RESET_ALL}
"""
def acc():
    while True:
        clear()
        print(logo)
        print(menu)
        escolhas = input("Digita: ")
        if escolhas == "1":
            clear()
            verfy()
        elif escolhas == "2":
            clear()
            generator()
        elif escolhas == "3":
            kitty_hello()
        elif escolhas == "4":
            clear()
            break
        input("...")
        clear()


if __name__ == "__main__":
    acc()