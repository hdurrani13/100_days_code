class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickels" : 0.05,
        "pennies" : 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        '''Prints the current profit'''
        print(f"Money: {self.CURRENCY}{self.profit:.2f}")
    
    def process_coins(self):
        '''Returns the total calculated coins inserted'''
        print("Payment Please!")
        self.money_recieved = 0

        for coin in self.COIN_VALUES:
            num_of_coins = int(input(f"How many {coin}?: "))
            self.money_recieved += num_of_coins * self.COIN_VALUES[coin]
        
        return self.money_recieved

    def make_payment(self, cost):
        '''Returns True when payment is accepted'''
        self.process_coins()

        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost, 2)

            if change > 0:
                print(f"Here is {self.CURRENCY}{change:.2f} in change.")
            
            self.profit += cost
            self.money_recieved = 0
            return True 
        
        print(f"Sorry, {cost} not enough. Money Refunded!")
        self.money_recieved = 0
        return False
    
        

