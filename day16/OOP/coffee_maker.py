class CoffeeMaker:
    '''Models the machine that makes the coffee'''
    def __init__(self):
        self.resources = {
            "water" : 300,
            "milk" : 200,
            "coffee" : 100
        }

    def report(self):
        '''Prints report of all resources'''
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def check_resources(self, drink):
        '''Returns True when order can be made, False if ingridients are insufficient'''
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry, There is not enough {ingredient}!")
                return False
        return True

    def make_coffee(self, order):
        '''Deducts the required ingredients from the resource'''
        for ingredient in order.ingredients:
            self.resources[ingredient] -= order.ingredients[ingredient]
        
        print(f"Here is your {order.name}, enjoy!")
        

