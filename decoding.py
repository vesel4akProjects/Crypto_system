from cryptography.fernet import Fernet
from pyperclip import copy
from sys import exit

FILE = "key_crypt.txt"
ENCRYPT_FILE = "encrypt_data.txt"

def decode_message(data):
    try:

        with open(FILE, "rb") as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        with open(ENCRYPT_FILE, "rb") as d:
            data = d.read()


        decrypted_data = cipher.decrypt(data)
        print(f"The decrypted message : {decrypted_data.decode()}\n\n")

        choice = input("Do you want to decrypt the message again ? (y/n) : ").lower()

        if choice == "y":

            with open(ENCRYPT_FILE, "rb") as d:
                data = d.read()


            decode_message(data)

        elif choice == "n":

            choice = input("Do you want to copy the decrypted message to the clipboard ? (y/n) : ").lower()

            if choice == "y":

                copy(str(decrypted_data.decode()))
                print("The decrypted message has been successfully saved to the clipboard !\n\n")




            elif choice == "n":
                exit(0)

            else:
                print("This option is not available !")

        else:
            print("This option is not available !")

    except (FileNotFoundError,FileExistsError):

        key = input("Since the file with the encryption key has not been found or has not been created, enter the encryption key : ")
        cipher = Fernet(key)

        decrypted_data = cipher.decrypt(data)
        print(f"The decrypted message : {decrypted_data.decode()}\n\n")

        choice = input("Do you want to decrypt the message again ? (y/n) :").lower()

        if choice == "y":

            with open(ENCRYPT_FILE, "rb") as d:
                data = d.read()

            decode_message(data)

        elif choice == "n":

            choice = input("Do you want to copy the decrypted message to the clipboard ? (y/n) : ").lower()

            if choice == "y":

                copy(str(decrypted_data.decode()))
                print("The decrypted message has been successfully saved to the clipboard !\n\n")



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
        with open(ENCRYPT_FILE, "rb") as d:
            data = d.read()

        decode_message(data)

    except Exception as e:
        print(f"Error : {e}")