import string
import random
import datetime
import os
from cryptography.fernet import Fernet

#pseudo-random password
def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))

#function that writes key one time
def load_create_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key


def main():
    
    pass_length = 0
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    save_choice = "n"
    service_name = ""

#pass generating loop
    while True: 
        try:   
            print("Hey, I can generate password. Enter password length (must be at least 5 characters):")
            pass_length = int(input())
            if pass_length > 4:
                password = pass_gen(pass_length)
                print(f"Your new password is: {password}\n")
                break
    
        except ValueError:
            print("Please enter a valid number.")

#entering service name for password
    try:
        print("Which service or platform is this password for? (Discord, Gmail etc.):")
        service_name = input()
        #possible char limit to add.
    except ValueError:
        print("Invalid service name.")
    
#encrypt and save loop
    while True:

        try:
            print("Do you want to encrypt and save your password? y/n")
            save_choice = input()
            if save_choice == "n":
                return
            elif save_choice == "y":
                key = load_create_key()#creating or using existing key
                cipher = Fernet(key)#loading key
                encrypted_password = cipher.encrypt(password.encode())#encrypting password

                with open("my_passwords.txt", "a") as file:
                    file.write(f"{current_time} | {service_name} | {encrypted_password}\n")

                break
            else:
                print("Sorry, wrong answer.")

        except ValueError:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
