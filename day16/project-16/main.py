from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()

while True:
    request = input(f"What would you like? ({menu.get_items()}): ").lower()

    if request == "off":
        # Turns the coffee machine off
        break

    elif request == "report":
        # Prints a report of the current resources
        coffe_maker.report()
        money_machine.report()

    else:
        # Processes the request
        drink = menu.find_drink(request)
        if not drink:
            continue

        # Checks if the resources are available for the request
        if not coffe_maker.is_resource_sufficient(drink):
            continue

        # Makes the payment
        if not money_machine.make_payment(drink.cost):
            continue

        coffe_maker.make_coffee(drink)
