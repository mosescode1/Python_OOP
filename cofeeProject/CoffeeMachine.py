from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice in ['off','OFF', "Off"]:
        machine_on = False
    elif choice == 'report':
        make_coffee.report()   
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               make_coffee.make_coffee(drink)