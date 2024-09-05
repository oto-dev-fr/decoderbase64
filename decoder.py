import base64
import logging
from colorama import Fore, Style, init

init(autoreset=True)

class color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    while True:
        token = input(f"{color.GREEN}[!] {color.WHITE}Veuillez entrer le jeton (format : hachage:base64) : {color.RESET}").strip()
        if not token:
            print(f"{color.RED}[!] {color.WHITE}Réponse invalide. Le jeton ne peut pas être vide.{color.RESET}")
            continue
        
        try:
            encoded_string = token.split(':')[1]
            decoded_string = base64.b64decode(encoded_string).decode('utf-8')
            print(f"{color.GREEN}[+] {color.WHITE}La chaîne décodée est : {decoded_string}{color.RESET}")
            break 
        except IndexError:
            print(f"{color.RED}[!] {color.WHITE}Erreur : Le jeton fourni ne semble pas être au format attendu (hachage:base64).{color.RESET}")
        except base64.binascii.Error:
            print(f"{color.RED}[!] {color.WHITE}Erreur : La partie Base64 du jeton est invalide.{color.RESET}")
        except Exception as e:
            print(f"{color.RED}[!] {color.WHITE}Une erreur s'est produite : {e}{color.RESET}")
    input(f"{color.GREEN}[!] {color.WHITE}Appuyez sur ENTER pour quitter...{color.RESET}")

title = color.RED + '''
▓█████▄ ▓█████  ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▀███  
▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░    ░   ░        ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
   ░       ░  ░░ ░          ░ ░     ░       ░  ░   ░     
 ░             ░                  ░                      
''' + color.WHITE + "fully coded by oto.dev" + color.RESET  
print(title)

if __name__ == '__main__':
    main()
