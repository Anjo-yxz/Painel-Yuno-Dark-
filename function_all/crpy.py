import os
import base64
import hashlib
from colorama import Fore,Style
from cryptography.fernet import Fernet

logo = f"""{Fore.LIGHTMAGENTA_EX}
                ▓██   ██▓ █    ██  ███▄    █  ▒█████       ██▓    ▒█████    ▄████▄  ██ ▄█▀
                 ▒██  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒    ▓██▒   ▒██▒  ██▒ ▒██▀ ▀█  ██▄█▒ 
                  ▒██ ██░▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒    ▒██░   ▒██░  ██▒ ▒▓█    ▄▓███▄░ 
                  ░ ▐██▓░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░    ▒██░   ▒██   ██░▒▒▓▓▄ ▄██▓██ █▄ 
                  ░ ██▒▓░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░    ░██████░ ████▓▒░░▒ ▓███▀ ▒██▒ █▄
                   ██▒▒▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ░ ▒░▓  ░ ▒░▒░▒░ ░░ ░▒ ▒  ▒ ▒▒ ▓▒
                 ▓██ ░▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░     ░ ░ ▒    ░ ▒ ▒░    ░  ▒  ░ ░▒ ▒░
                 ▒ ▒ ░░   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒        ░ ░  ░ ░ ░ ▒   ░       ░ ░░ ░ 
                 ░ ░        ░              ░     ░ ░          ░      ░ ░   ░ ░     ░  ░   {Style.RESET_ALL}
"""
menu = f"""{Fore.LIGHTMAGENTA_EX}  
                                      Y U N O   L O C K             
                                    "Onde seus dados morrem"         
                            ==========================================
                            | [1] Criptografar Arquivo               |
                            | [2] Descriptografar Arquivo            |
                            | [3] Sair do Sistema                    |
                            =========================================={Style.RESET_ALL}
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def aquivo_64(cam_p, main):
    try:
        with open(cam_p, "rb") as f:
            conteudo = f.read()

        dados_trancados = main.encrypt(conteudo)

        novo_nome = cam_p + ".locked"
        with open(novo_nome, "wb") as f:
            f.write(dados_trancados)

        os.remove(cam_p)
        print(f"\n{Fore.MAGENTA}[+] Yuno Gasai criptografou o arquivo: {cam_p} :3{Style.RESET_ALL}")
        input("")
    except FileNotFoundError:
        print(f"{Fore.RED}\n[!] Erro: Arquivo não encontrado!{Style.RESET_ALL}")

def descriptografar_arquivo(cam_p, main):
    if not cam_p.endswith(".locked"):
        print("\n[!] Aviso: Selecione o arquivo .locked para descriptografar!")
        return

    try:
        with open(cam_p, "rb") as f:
            dados_trancados = f.read()
    
        dados_ori = main.decrypt(dados_trancados)
        nome_original = cam_p.replace(".locked", "")
        
        with open(nome_original, "wb") as f:
            f.write(dados_ori)
                   
        os.remove(cam_p)
        print(f"\n{Fore.MAGENTA}[+] Yuno recuperou o arquivo: {nome_original}{Style.RESET_ALL}")
        
    except Exception:
        print(f"\n{Fore.RED}[!] Senha incorreta ou arquivo corrompido! :({Style.RESET_ALL}")

def acc():
    while True:
        c_p = input("Senha do sistema: ")
        cam_p = input("Caminho do Arquivo: ")
        k_p = hashlib.sha256(c_p.encode()).digest()
        k_64 = base64.urlsafe_b64encode(k_p)
        main_engine = Fernet(k_64)
        print(logo)
        print(menu)
        
        escolha = input("Digita: ").lower()

        if escolha == "1":
            clear()
            aquivo_64(cam_p, main_engine)
        elif escolha == "2":
            clear()
            descriptografar_arquivo(cam_p, main_engine)
        elif escolha == "3":
            clear()
            print("Saindo... Até logo!")
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
        input("...")
        clear()

if __name__ == "__main__":
    acc()