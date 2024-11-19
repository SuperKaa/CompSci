import random

def getbal():
    with open("balance.txt", "r") as file:
        balance = file.read()
        return int(balance)

def writebal(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))

def rando():

    balance = getbal()
    print(f"you have £{balance}")
    print("it costs £1 to play one game! and you can type exit to exit.")
    balance = balance - 1
    if balance <= 0:
        print("your too broke to play this game, go get some money first!")
        return
    writebal(balance)

    choices = ["apple", "pear", "star", "skull", "heart"] 

    spin = random.choices(choices, k=3)
    print("Spinning")
    print("Result: ", " | ".join(spin))
      
    if spin[0] == spin[1] == spin[2]:  
        if spin[0] == "star":
            print("you win 5")
            balance = balance +5
            writebal(balance)
        print("you win 2")
        balance = balance +2
        writebal(balance)
    elif spin[0] == spin[1] or spin[0] == spin[2] or spin[1] == spin[2]:   
        print("you win £1")
        balance = balance +1
        writebal(balance)
    else:
        print("loser loser")

while True:

    iinput = input("press enter to spin or exit to exit\n").lower()

    if iinput == 'exit':
        print("bye dont lose next time (:")
        break
    else:
        rando()
