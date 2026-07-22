# Coffee Machine
# Day 15
# ----------------------------------------------#

# menu dictionary for coffee machine
MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

print("\n")
print('*' * 30)
print("Welcome to the Coffee Machine!")
print('*' * 30)

def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(order_ingredients):
    '''Returns True is there is sufficent ingredients'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coins():
    '''Returns the total calculated coins inserted'''
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transcation_successful(money_received, drink_cost):
    '''Returns True when payment is accepted, False otherwise'''
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else: 
        print(f"Sorry {money_received} not enough money. Money Refuned")
        return False
    
def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️.")

is_on = True 
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        report(resources)
    else:
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if is_transcation_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])



