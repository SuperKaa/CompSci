import random
import time
import os

one = random.randint(10,99)
two = random.randint(10,99)
three = random.randint(10,99)
four = random.randint(10,99)
five = random.randint(10,99)
six = random.randint(10,99)
seven = random.randint(10,99)
eight = random.randint(10,99)
nine = random.randint(10,99)

tried = []

while True:
    num = random.randint(10,99)

    if num in tried:
       continue

    tried.append(num)

    os.system("cls")

    grid = f"number called is {num}\n\ncurrent grid is:\n{one} {two} {three}\n{four} {five} {six}\n{seven} {eight} {nine}"
    print(grid)
    time.sleep(0.5)

    if num == one:
       one = "X"
    if num == two:
       two = "X"
    if num == three:
       three = "X"
    if num == four:
       four = "X"
    if num == five:
       five = "X"
    if num == six:
       six = "X"
    if num == seven:
       seven = "X"
    if num == eight:
       eight = "X"
    if num == nine:
       nine = "X"

    if one == "X" and two == "X" and three == "X" and four == "X" and five == "X" and six == "X" and seven == "X" and eight == "X" and nine == "X":
       break

print("BINGO")
time.sleep(5)
