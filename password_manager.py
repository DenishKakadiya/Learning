from cryptography.fernet import Fernet



#need only once
""" def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() """
        
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read("key.key")
        return key

master_pwd = input("Please enter the master passwrod : ")
key = load_key() + master_pwd.bytes
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"Username: {user}, Password: {far.decrypt(passw.encdode)}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:   
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input ("Do you want to add a new password or review an existing password (view, add), press 'q' to Quit: ").lower()
    if (mode == "q"):
        break
    elif (mode == "view"):
        view()
    elif (mode == "add"):
        add() 
    else:
        print("Invalid mode.!")
        continue
