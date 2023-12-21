from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")
mode = input("Would you like to add a new password or view existing ones (view, add)? (Press q to quit) ").lower()

# NOT FINISHED BECAUSE OF THE LACK OF '_cffi_backend' MODULE

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}| Password: {passw}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')


while True:
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")