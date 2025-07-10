from cryptography.fernet import Fernet
from pyperclip import copy
from sys import exit


FILE = "key_crypt.txt"

def encrypt_message(data : str):
    try:
        with open(FILE, "rb") as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        data = f"{data}".encode()
        encrypted_data = cipher.encrypt(data)
        print(f"Encrypted message : {encrypted_data}")

        decrypted_data = cipher.decrypt(encrypted_data)
        print(f"The source text of the image : {decrypted_data.decode()}")

        choice = input("Do you want to encrypt the message again ? (y/n) : ").lower()

        if choice == "y":

            data = input("Enter the message to encrypt : ")
            encrypt_message(data)

        elif choice == "n":
            choice = input("Do you want to copy an encrypted message to the clipboard ? (y/n) : ").lower()

            if choice == "y":

                copy(encrypted_data)
                print("The encrypted message has been successfully saved to the clipboard !\n\n")

            elif choice == "n":
                exit(0)

            else:
                print("This option is not available !")


        else:
            print("This option is not available !")

    except (FileNotFoundError,FileExistsError):

        key = input("Since the file with the encryption key has not been found or has not been created, enter the encryption key : ")
        cipher = Fernet(key)

        data = f"{data}".encode()
        encrypted_data = cipher.encrypt(data)

        print(f"Encrypted message : {encrypted_data}")

        decrypted_data = cipher.decrypt(encrypted_data)
        print(f"The source text of the image : {decrypted_data.decode()}\n\n")

        choice = input("Do you want to encrypt the message again ? (y/n) : ").lower()

        if choice == "y":

            data = input("Enter the message to encrypt : ")
            encrypt_message(data)

        elif choice == "n":
            choice = input("Do you want to copy an encrypted message to the clipboard ? (y/n) : ").lower()

            if choice == "y":

                copy(str(encrypted_data))
                print("The encrypted message has been successfully saved to the clipboard !\n\n")

            elif choice == "n":
                exit(0)

            else:
                print("This option is not available !")


        else:
            print("This option is not available !")


    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    try:
            data = input("Enter the message to encrypt : ")
            encrypt_message(data)

    except Exception as e:
        print(f"Error : {e}")

