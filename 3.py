# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

def calculator_add():
    result = first_number + second_number
    print(f"Result : {result}")
def calculator_substract():    
    result = first_number - second_number
    print(f"Result : {result}")
def calculator_multiple():    
    result = first_number * second_number
    print(f"Result : {result}")
def calculator_divide():    
    result = first_number / second_number
    print(f"Result : {result}")

if operation.lower() == "add":
    calculator_add()
elif operation.lower() == "subtract":
    calculator_substract()
elif operation.lower() == "multiple":
    calculator_multiple()
elif operation.lower() == "divide":        
    calculator_divide()      
else:
    print("Sorry, I do not understand your request.")

