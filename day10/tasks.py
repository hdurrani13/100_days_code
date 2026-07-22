## Function and Inputs 
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return print("nothing was entered\n")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"Result: {formated_f_name} {formated_l_name}"

formated_string = format_name("hamZa", "DURRANI")

# print(formated_string)
'''
def fun_1(text):
    return text + text

def fun_2(text):
    return text.title()

output = fun_2(fun_1("hello"))
print(output)
'''

## Docstrings 
# ex.
"""Take a first name and last name and format it 
to be return the title case version of the name."""

print(format_name(input("What is your first name? "), input("What is you last name? ")))
