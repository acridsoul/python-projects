print("Welcome to The Game of the Goats")
print("Play if You Dare! ")
answer = input("Wanna play? Yes or No \n").lower()

count = 0

if answer == "no":
    exit()
else:
    print("Let's Go")

midfielder = input("KDB OR KROOS? ").lower().upper()
if midfielder == "KDB":
    print("Next Question")
    count += 1
else:
    print("Game Over, You are Noob")
    exit()

centre_back = input("DIAS OR MILITAO? ").lower().upper()
if centre_back == "DIAS":
    print("Next Question")
    count += 1
else:
    print("Game Over, You are Noob")
    exit()

striker = input("LEWA OR HAALAND? ").lower().upper()
if striker == "LEWA":
    print("Next Question")
    count += 1
else:
    print("Game Over, You are Noob")
    exit()

goat = input("MESSI OR RONALDO? ").lower().upper()
if goat == "RONALDO":
    print("You Won! ")
    count += 1
else:
    print("Game Over, You are Noob")
    exit()

print(count)