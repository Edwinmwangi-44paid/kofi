menu = {
    "espresso": {
        "ingredients": {
             "water": 50,  # in milliliter
             "coffee": 18  # in grams
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,  # in milliliters
            "milk": 0,    # in milliliters
            "coffee": 18  # in grams
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,  # in milliliters
            "milk": 100,    # in milliliters
            "coffee": 24,  # in grams
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
""""Returns true when orders can be made and false if the order ingredinest are insufficient"""
def is_resource_sufficient(order_ingredients):
    """"Returns true when orders can be made and false if the order ingredinest are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("sorry there is no enough {item}.")
            return False
    return True


def is_transaction_sucessful(money_received, drink_cost):
    """Return true if the payments is succesfull and false if the payments is failed"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that is not enough money. Money refunded.")
        return False
    


def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total = int(input("how many dime?: ")) * 0.1
    total = int(input("how many nickles?: ")) * 0.05
    total = int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} 😊")
is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
         print(f"water: {resources['water']}ml")
         print(f"milk: {resources['milk']}ml")
         print(f"coffee: {resources['coffee']}ml")
         print(f"money: {profit}" )
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payments = process_coins()
            if is_transaction_sucessful(payments, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

        
