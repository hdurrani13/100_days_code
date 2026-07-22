# Scope 
enemies = 1 

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies ouside function: {enemies}")

# Global Scope
player_health = 10 # This variable is global 

# Local Scope
def drink_potion():
    potion_strenght = 2 # This variable is a local variable "Local Scope"
    print(potion_strenght)
    print(player_health)

drink_potion()

print("###########################")

# Coding Exercise: Prime number checker
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(75))
