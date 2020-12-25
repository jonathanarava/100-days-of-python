from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    selected = input(f"What would you like? ({options}): ")
    # TODO #1: Print report
    if selected == "report".lower():
        coffee_maker.report()
        money_machine.report()

    elif selected == "off".lower():
        is_on = False

    else:
        drink = menu.find_drink(selected)
        # TODO #2: Check resources sufficient
        # TODO  # 3: Process coins
        # TODO #4: Check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink) # TODO #5: Make Coffee




