class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def read_number_served(self):
        print(f"No of people served for {self.name} is: {self.number_served}")   

    def set_number_served(self, people):
        self.number_served = people

    def increment_number_served(self, peeps):
        self.number_served += peeps

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}")
        print(f"The cuisine type is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open")

# Creating instances of the Restaurant class
restaurant = Restaurant("Kempinski", "Japanese")
restaurant1 = Restaurant("Trump Hotel", "Chinese")
restaurant2 = Restaurant("BlaBla Hotel", "Italian")

# Printing the attributes individually
print(restaurant.name)  # Output: Kempinski
print(restaurant.type)  # Output: Japanese

# Working with number_served
restaurant.read_number_served()
restaurant.set_number_served(23)
restaurant.read_number_served()
restaurant.increment_number_served(100)
restaurant.read_number_served()

# Calling methods for each instance
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, identity, residence):
        self.first_name = first_name
        self.last_name = last_name
        self.id = identity
        self.residence = residence
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"Names are {self.first_name} {self.last_name} Id is {self.id} He lives in {self.residence} ")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

# Creating an instance of the User class
user = User("Mark", "Twain", 455677, "Bangladesh")

user.greet_user()
user.describe_user()

# Working with login_attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # Output: 3

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # Output: 0