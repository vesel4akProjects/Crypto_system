from cryptography.fernet import Fernet
from pyperclip import copy
from sys import exit

FILE = "key_crypt.txt"


def generate_key():

    try:

        key = Fernet.generate_key()

        with open(FILE,"wb") as key_file:
            print(f"The encryption key : {key.decode()}")
            key_file.write(key)
            print(f"the encryption key was successfully saved to the file {FILE} !\n\n")

        choice = input("Do you want to generate the encryption key again ? (y/n) : ").lower()

        if choice == "y":
            generate_key()

        elif choice == "n":
            choice = input("Do you want to copy the encryption key to the clipboard ? (y/n) : ").lower()

            if choice == "y":

                with open(FILE, "rb") as key_file:

                    key = key_file.read()
                    copy(str(key))

                    print("The encryption key has been successfully saved to the clipboard !")

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

        generate_key()

    except Exception as e:
        print(f"Error : {e}")


