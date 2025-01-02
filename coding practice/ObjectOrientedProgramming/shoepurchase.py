from Shoes import Shoes

low = Shoes("Nike", 100)
medium = Shoes("Adidas", 200)
high = Shoes("Reebok", 300)

try:
    shoe_budget = float(input("Enter your budget: "))
except ValueError:
    exit("Budget must be a number!")

for shoes in [high, medium, low]:
    shoes.buy(shoe_budget)