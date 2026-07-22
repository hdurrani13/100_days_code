def greet():

    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")


# greet()

# Functions with inputs

def greet_with_names(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# greet_with_names('hamza')

def life_in_weeks(age):
    live_till = 90
    live_left = (live_till - age) * 52
    print(f"You have {live_left} weeks left.")

# life_in_weeks(56)

# Function with two parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("hamza","Canada")
greet_with(location="hamza",name="Canada")