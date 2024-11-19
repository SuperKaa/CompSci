from colorama import *
import time

init(autoreset=True)

def guess():

    print(Fore.CYAN + """
mammals = horse, cow, sheep, dog, cat, lion, tiger
birds = penguin, ostrich, sparrow
insects = spider, ant, wasp

please choose a random animal

""")

    mammals = ["horse", "cow", "sheep", "dog", "cat", "lion", "tiger"]
    birds = ["penguin", "ostrich", "sparrow"]
    insects = ["spider", "ant", "wasp"]
    types = ["mammal", "bird", "insect"]

    while True:
        type = input(Fore.CYAN + "is your animal a mammal/bird/insect ").lower()

        if type in types:
            break
        else:
            print(Fore.RED + "are you sure you typed that correctly?")

    if type == "mammal":
        while True:
            letter = input(Fore.CYAN + "what does the name of the animal begin with? ").lower()
            letters = ["h", "c", "s", "d", "l", "t"]
            if letter in letters:
                break
            else:
                print(Fore.RED + "are you sure you typed that correct?")
        
        if letter == "h":
            print(Fore.GREEN + "your animal is a horse!!")
            
        elif letter == "c":
            while True:
                isit = input(Fore.CYAN + "is your animal a cow? (yes/no)").lower()

                if isit in ["yes", "no"]:
                    break
                else:
                    print(Fore.RED + "are you sure you typed that correctly?")

            if isit == "yes":
                print(Fore.GREEN + "i knew it!!!")

            elif isit == "no":
                print(Fore.GREEN + "your animal is a cat!")
        elif letter == "s":
            print(Fore.GREEN + "your animal is a sheep!!")
        elif letter == "d":
            print(Fore.GREEN + "your animal is a dog!!!")
        elif letter == "l":
            print(Fore.GREEN + "your animal is a lion!")
        elif letter == "t":
            print(Fore.GREEN + "your animal is a tiger!!")

    if type == "bird":
        while True:
            isit = input(Fore.CYAN + "can the bird fly? (yes/no) ").lower()

            if isit in ["yes", "no"]:
                break
            else:
                print(Fore.RED + "are you sure you typed that correctly?")

        if isit == "yes":
            print(Fore.GREEN + "your animal was a sparrow!")
        elif isit == "no":
            while True:
                isit1 = input(Fore.CYAN + "does your animal name begin with 'p'? ").lower()
                if isit1 in ["yes", "no"]:
                    break
                else:
                    print(Fore.RED + "are you sure you typed that correctly?")

            if isit1 == "yes":
                print(Fore.GREEN + "your animal is a penguin!!!!")

            elif isit1 == "no":
                print(Fore.GREEN + "your animal is an ostrich!!!!!!!")

    if type == "insect":
        while True:
            isit = input(Fore.GREEN + "can the insect fly? ").lower()

            if isit in ["yes", "no"]:
                break
            else:
                print(Fore.RED + "are you sure you typed that correctly?")

        if isit == "yes":
            print(Fore.GREEN + "your animal is a wasp!")
        elif isit == "no":

            while True:
                isit1 = input(Fore.CYAN + "how many legs does this insect have, 8 or 6? ").lower()

                if isit1 in [8, 6]:
                    break
                else:
                    print(Fore.RED + "are you sure you typed 8 or 6?")

            if isit1 == "8":
                print(Fore.GREEN + "your animal is a spider!")
            elif isit1 == "6":
                print(Fore.GREEN + "your animal is an ant!!")

guess()
time.sleep(5)
