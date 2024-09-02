import base64

def main():
    token = input("Veuillez entrer le jeton (format : hachage:base64) : ")

    try:
        encoded_string = token.split(':')[1]
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')
        print(f"La chaîne décodée est : {decoded_string}")

    except IndexError:
        print("Erreur : Le jeton fourni ne semble pas être au format attendu (hachage:base64).")
    except base64.binascii.Error:
        print("Erreur : La partie Base64 du jeton est invalide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    input("\nAppuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()