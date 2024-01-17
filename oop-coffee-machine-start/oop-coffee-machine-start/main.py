from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

me = Menu()

co = CoffeeMaker()
mo = MoneyMachine()


t = True
while t:

    ty = input("What Would You Like? (espresso/latte/cappuccino):").lower()
    if ty == 'off':
        t = False
    elif ty == 'report':
        co.report()
        mo.report()
    elif ty == 'espresso':
        options = me.find_drink(ty)
        if co.is_resource_sufficient(me.find_drink(ty)) and mo.make_payment(options.cost):

            co.make_coffee(mo.find_drink(ty))
    elif ty == 'latte':
        options = me.find_drink(ty)
        if co.is_resource_sufficient(me.find_drink(ty)) and mo.make_payment(options.cost):

            co.make_coffee(me.find_drink(ty))
    elif ty == 'cappuccino':
        options = me.find_drink(ty)
        if co.is_resource_sufficient(me.find_drink(ty)) and mo.make_payment(options.cost) :
            co.make_coffee(me.find_drink(ty))

