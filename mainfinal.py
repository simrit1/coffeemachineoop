from finalmenu import Menu, MenuItem
from finalcoffeemaker import CoffeeMaker
from finalcashier import Cashier

def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE KEA COFFEE MACHINE!
          `-----' 
    
          ------ MENU ------ 
          Latte (30 DKK)
          Espresso (20 DKK)
          Cappuccino (25 DKK)
          Americano (25 DKK)
          ------------------
    
          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')


menu = Menu()
finalcashier = Cashier()
finalcoffeemaker = CoffeeMaker()
is_on = True

while is_on:
    welcome()
    options = menu.get_items()
    user_choice = (input(f'What would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print("Have a KEAlicious day!")
        is_on = False
    elif user_choice == 'report':
        finalcoffeemaker.report()
        finalcashier.report()
    elif menu.find_drink(user_choice) is None:
        print("Please choose an available option.")
    else:
        beverage = menu.find_drink(user_choice)
        sufficient_resources = finalcoffeemaker.is_resource_sufficient(beverage)
        sufficient_money = finalcashier.make_payment(beverage.cost)
        if sufficient_resources and sufficient_money:
            print('Payment accepted! Making your beverage now')
            finalcoffeemaker.make_coffee(beverage)