import random
import time
from colorama import *

init(autoreset = True)

print(Fore.CYAN + """
-----------------------------------
|                                 |
|      |USERNAME GENERATOR|       |
|                                 |
-----------------------------------

""")

name = input(Fore.MAGENTA + "first name? ")
lastname = input(Fore.MAGENTA + "last name? ")
dob = input(Fore.MAGENTA + "year of birth?")

name = name[0:2]
lastname = lastname[0:3]
dob = dob[-2:]

print(Fore.GREEN + f"\nyour ideal username is {name}{lastname}{dob}\n")


while True:
    option = input(Fore.MAGENTA + "do you want more random numbers on the end? (yes/no)").lower()

    if option == "yes":
        print(Fore.GREEN + "adding random numbers...")
        time.sleep(1)
        rand = random.randint(10,99)
        print(Fore.GREEN + f"your new username is {name}{lastname}{dob}{rand}")
        time.sleep(5)
        break

    elif option == "no":
        print(Fore.RED + "random numbers will not be added")
        time.sleep(5)
        break

    else:
        print(Fore.RED + "please enter a valid option (yes/no) \n")
