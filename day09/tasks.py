# Dictionary
#-----------------------------------------------#
programming_dictionary = {
    "Bug": "An error in a program.",
    "Function": "Code you can call over and over again.", 
    "Loop": "Doing something over and over again."
}

# print(programming_dictionary["Bug"])

# Adding new entry to the dictonary
programming_dictionary["Hamza"] = "Beautiful Man"
# print(programming_dictionary)

# Wipe an existing dictionary 
'''programming_dictionary = {}
print(programming_dictionary)'''

# Edit an item in a dictoionary 
'''programming_dictionary["Bug"] = "A moth"
print(programming_dictionary)'''

# Looping through a dictionary 
'''for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])'''

'''for key, i in programming_dictionary.items():
    print(f"{key}: {i}")'''

#------------------------------------------------------#
# Practice
'''
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for grades in student_scores.items():
    if grades[1] >= 91 and grades[1] <= 100:
        student_grades[grades[0]] = "Outstanding"
    elif grades[1] >= 81 and grades[1] <= 90:
        student_grades[grades[0]] = "Exceeds Expectations"
    elif grades[1] >= 71 and grades[1] <= 80:
        student_grades[grades[0]] = "Acceptable"
    elif grades[1] <= 70:
        student_grades[grades[0]] = "Fail"
print(student_grades)
'''

# Nested List and Dictionary 
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
'''
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][2]) # Dijon  
'''
# Nested list
'''
nested_list = ["A","B", ["C","D"]]
print(nested_list[2][1]) # Prints 'D'
'''

# for key, i in travel_log.items():
#     print(key)
#     print(i)

travel_log = {
    "France": {
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12
    },
    "Germany": {
        "Cities_visited": ["Stuttgart", "Berlin", "Hamburg",],
        "Total_visits": 5
    },
}

print(travel_log["Germany"]["Cities_visited"][0])