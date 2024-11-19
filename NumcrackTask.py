import random
from colorama import*
import time

init(autoreset=True)

num = 0

while num > 999 or num < 111:
    num = int(input("Enter a random number between 111 and 999 "))
    if num > 999 or num < 111:
        print(f"\n{num} is not between 111 and 999")

gen = 0
i = 0
tried = []

while num != gen:

    gen = random.randint(111, 999)
    if gen in tried:
        continue
    tried.append(gen)
    i += 1
    if num != gen:
        print(Fore.RED + str(gen))
    if num == gen:
        print(Fore.GREEN + f"Number {num} has been cracked in {i} attempts")
        time.sleep(5)
        
