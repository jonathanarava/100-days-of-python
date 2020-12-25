MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,  # added this line
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
}

coins_in_machine = {
    "quarters": {
        "value": 0.25,
        "quantity": 0,
    },
    "dimes": {
        "value": 0.10,
        "quantity": 0,
    },
    "nickels": {
        "value": 0.05,
        "quantity": 0,
    },
    "pennies": {
        "value": 0.01,
        "quantity": 0,
    },

}


def print_report():
    """ Displays the resources and the amount of resources in the machine. """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_coins_in_machine()}")


def transaction():
    """ Machine accepts coins and returns change, if user gives excess. """
    # add coins
    coins_in_machine['quarters']['quantity'] += num_quarters
    coins_in_machine['dimes']['quantity'] += num_dimes
    coins_in_machine['nickels']['quantity'] += num_nickels
    coins_in_machine['pennies']['quantity'] += num_pennies
    # Offers change to user
    if total_user_coins > MENU[selected]['cost']:
        change = round(total_user_coins - MENU[selected]['cost'], 2)
        offer_change(change)
        print(f"Here is ${change} in change.")
    return True


def check_sufficient_money():
    """ Checks whether user has sufficient coins for drink. """
    if total_user_coins >= MENU[selected]['cost']:
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def check_sufficient_resources():
    """ Checks whether the machine has sufficient resources (i.e. water, milk, coffee)
     in order to make user selected drink. """
    sufficient_res = True
    for key in MENU[selected]['ingredients']:
        if resources[key] < MENU[selected]['ingredients'][key]:
            print(f"Sorry there is not enough {key}.\n")
            sufficient_res = False
    return sufficient_res


def offer_change(amount):
    """ Dispenses excess amount given by user strictly with available coins  (i.e. 2 quarter,
    0 dimes, 1 nickel, 0 pennies).  """
    print("\nDispensing excess amount: ")
    for key in coins_in_machine:
        counter = 0
        while coins_in_machine[key]['quantity'] > 0 and amount // coins_in_machine[key]['value'] > 0:
            coins_in_machine[key]['quantity'] -= 1
            amount -= coins_in_machine[key]['value']
            amount = round(amount, 2)
            counter += 1
        print(f"Dispensed {counter} {key}")
        # print(f"amount carried forward: {amount}")


def sum_coins(quarters, dimes, nickels, pennies):
    """ Returns the sum of coins. """
    sum_quarters = coins_in_machine['quarters']['value'] * quarters
    sum_dimes = coins_in_machine['dimes']['value'] * dimes
    sum_nickels = coins_in_machine['nickels']['value'] * nickels
    sum_pennies = coins_in_machine['pennies']['value'] * pennies

    return sum_quarters + sum_dimes + sum_nickels + sum_pennies


def total_coins_in_machine():
    """ Returns the sum  of coins in the machine. """
    return sum_coins(coins_in_machine['quarters']['quantity'],
                     coins_in_machine['dimes']['quantity'],
                     coins_in_machine['nickels']['quantity'],
                     coins_in_machine['pennies']['quantity'])


def make_drink():
    """ Dispenses the appropriate amount of resources to make the user selected drink. """
    # print(f"\nresources (before making drink): {resources}")
    for key in MENU[selected]['ingredients']:
        resources[key] -= MENU[selected]['ingredients'][key]
    # print(f"resources (after making drink): {resources}")


while True:
    total_user_coins = 0
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    selected = input("What would you like? (espresso/latte/cappuccino) ").lower()

    # TODO=: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if selected == "off":
        print("The machine is off.")
        break

    # TODO=: 3. Print report
    elif selected == "report":
        print_report()

    else:
        # TODO=: 4. Check resources sufficient?
        sufficient_resources = check_sufficient_resources()

        # TODO=: 5. Process coins.
        if sufficient_resources:
            print("Please insert coins...")
            num_quarters = int(input("How many quarters?: "))
            num_dimes = int(input("How many dimes?: "))
            num_nickels = int(input("How many nickels?: "))
            num_pennies = int(input("How many pennies?: "))
            total_user_coins = sum_coins(quarters=num_quarters,
                                         dimes=num_dimes,
                                         nickels=num_nickels,
                                         pennies=num_pennies)

        # TODO=: 6. Check transaction successful?
        sufficient_money = check_sufficient_money()

        # TODO=: 7. Make  Coffee
        if sufficient_money:
            transaction()
            make_drink()
            print(f"\nHere is your {selected} ☕. Enjoy!")
