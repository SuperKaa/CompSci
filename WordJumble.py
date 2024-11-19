import random
import time

print("CTRL + C to exit")
word = input("enter your word ").lower()

length = len(word)

vowels = ["a", "e", "i", "o", "u"]
alphabet = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


while True:
    rando = random.randint(0, int(length-1))
    letter = word[rando]

    if letter in vowels:
        word = word.replace(letter, "*")
    elif letter == "£":
        word = word.replace("£", "%")
    elif letter == " ":
        word = word
    elif letter in alphabet:
        word = word.replace(letter, "£")


    print(word)
    time.sleep(0.05)
