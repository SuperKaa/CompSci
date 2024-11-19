import base64
import time

print("""
-----------------------------------
|                                 |
|       |PASSWORD MANAGER|        |
|                                 |
-----------------------------------
""")

def decode(string):
    decoded = str(base64.b64decode(string))
    decoded = decoded[2:-1]
    return decoded

def encode(input):
    encode = str(base64.b64encode(input.encode()))
    encode = encode[2:-1]
    return encode

def enter():
    while True:
        decoded = readtxt()
        decoded = str(base64.b64decode(decoded))
        decoded = decoded[2:-1]
        decode = input("enter password ")
        if decode == decoded:
            print("correct password entered")
            break
        else:
            print("try again")

def writetxt(newpass):
    txt = open("encoded.txt", "w")
    txt.write(newpass)
    txt.close()

def readtxt():
    txt = open("encoded.txt", "r")
    data = txt.read()
    txt.close()
    return  data

def choice():
    while True:
        choice = input("do you want to create a new password? (yes/no) ")
        if choice == "no" or choice == "yes":
            break
        else:
            print("are you sure you entered yes/no?")

    if choice == "no":
        return

    if choice == "yes":
        txtread = readtxt()
        txtdecode = decode(txtread)

    while True:
        oldpass = input("enter your old password to confirm or type 'cancel' to cancel password change ")
        if oldpass == txtdecode:
            print("correct password entered")
            newpassword1 = input("enter your new password ")
            newpassword2 = input("enter your new password again ")

            if newpassword1 == newpassword2:
                writetxt(encode(newpassword1))
                print("new password has been set")
                break

            if newpassword1 != newpassword2:
                print("you entered two different passwords")

        if oldpass == "cancel" or oldpass == "Cancel":
            break
        else:
            print("please try again")

choice()
enter()

time.sleep(5)
