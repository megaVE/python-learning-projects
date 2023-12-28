import art

def calculate(first_number, second_number, operation):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def tim(a, b):
        return a * b

    def div(a, b):
        return a / b

    operators = {
        "+": add,
        "-": sub,
        "*": tim,
        "/": div,
    }

    return operators[operation](first_number, second_number)


result = None

print (art.logo)

while True:
    if result == None:
        first_number = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the next number?: "))

    result = calculate(first_number, second_number, operation)

    print(f"{first_number} {operation} {second_number} = {result}")
    keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    
    if(keep_result == 'y'):
        first_number = result
    else:
        result = None