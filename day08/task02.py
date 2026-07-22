# Love Calculator

def calculate_love_score(name1, name2):
    true_list = ["T", "R", "U", "E"]
    love_list = ["L", "O", "V", "E"]
    num1 = 0
    num2 = 0

    total_name = (name1 + name2).upper()

    for char in total_name:
        if char in true_list:
            num1 += 1
        if char in love_list:
            num2 += 1
    
    print(f"{num1}{num2}")
   

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")

