# Range Function with the for loop
# total = 0
# for i in range(1,101):
#     total += i 
#     # print(i)

# print(total)


for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print("Buzz")
    else:
        print(i)