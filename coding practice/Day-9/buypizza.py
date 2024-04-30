print("welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, L, M: ")
add_pepperoni = input("Do you want pepperoni? Y or N :  ")
extra_cheese = input("Extra Cheese Y or N : ")

'''
Small Pizza: $15
Medium Pizza: $20
Large pizza: $25

Pepperoni for small pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
'''

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


