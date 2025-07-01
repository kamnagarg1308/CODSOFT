def perform_add(a, b):
    return a + b

def perform_subtract(a, b):
    return a - b

def perform_multiply(a, b):
    return a * b

def perform_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("SIMPLE CALCULATOR")
print("==============================")
print("Choose an arithematic operation to perform:")
print("1 -> Addition")
print("2 -> Subtraction")
print("3 -> Multiplication")
print("4 -> Division")

while True:
    user_choice = input("Choose (1-4) or press 'q' to exit: ")

    if user_choice.lower() == 'q':
        print("Calculator closed. See you next time!")
        break

    if user_choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose from 1 to 4.")
        continue

    try:
        number1 = float(input("Enter first value: "))
        number2 = float(input("Enter second value: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if user_choice == '1':
        result = perform_add(number1, number2)
        print(f"Sum = {result}")
    elif user_choice == '2':
        result = perform_subtract(number1, number2)
        print(f"Difference = {result}")
    elif user_choice == '3':
        result = perform_multiply(number1, number2)
        print(f"Product = {result}")
    elif user_choice == '4':
        result = perform_divide(number1, number2)
        print(f"Quotient = {result}")

    print() 

