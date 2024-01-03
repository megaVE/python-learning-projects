MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def request_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def process_request(coffee_type):
    # Checks the available resources
    for resource in MENU[coffee_type]['ingredients']:
        if resources[resource] < MENU[coffee_type]['ingredients'][resource]:
            return print(f"Sorry. There is not enough {resource}.")

    # Checks the user's payment
    payment = round(request_money(), 2)

    exchange = payment - MENU[coffee_type]['cost']

    if exchange < 0:
        return print("Sorry. That's not enough money. Money refunded.")

    # Removes the used resources and returns the exchange
    for resource in MENU[coffee_type]['ingredients']:
        resources[resource] -= MENU[coffee_type]['ingredients'][resource]

    if exchange > 0:
        print(f"Here is ${exchange} dollars in charge.")

    print(f"Here is your {coffee_type}. Enjoy!")


while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")

    if request == "off":
        # Turns the coffee machine off
        break
    elif request == "report":
        # Prints a report of the current resources
        report()
    elif request in MENU:
        # Processes the request
        process_request(request)
    else:
        print("Invalid request!")
