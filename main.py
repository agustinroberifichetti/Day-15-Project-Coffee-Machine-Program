from data import MENU, resources

valid_options = ["espresso", "latte", "cappuccino", "report", "turn off machine"]


def ask_for_money():
    quarters = int(input("How many quarters? -> "))
    pennies = int(input("How many pennies? -> "))
    nickles = int(input("How many nickles? -> "))
    dimes = int(input("How many dimes? -> "))
    return quarters * 0.25 + pennies * 0.1 + nickles * 0.05 + dimes * 0.01


def check_resources_available(ingredients, current_resources):
    for ingredient in ingredients:
        if ingredients[ingredient] > current_resources[ingredient]:
            print(f"There is not enough {ingredient} to prepare your drink. Please, let know the manager")
            return False


def check_money(user_option, money_inserted):
    if money_inserted >= user_option['cost']:
        change = round(money_inserted - user_option['cost'], 2)
        print(f"Transaction successful. Your change is {change}.")
        for ingredient in user_option['ingredients']:
            resources[ingredient] -= user_option['ingredients'][ingredient]
        resources["money"] += user_option['cost']
        return resources
    else:
        print("Sorry, the money inserted is not enough for purchasing the selected beverage.")
        return resources


machine_in_process = True
while machine_in_process:
    user_option = input("What would you like to drink? (espresso / latte / cappuccino): ").lower()

    while user_option not in valid_options:
        user_option = input("\nThe input is not valid. Please, enter a valid option (espresso / latte / cappuccino): ")

    if user_option == "report":
        for resource in resources:
            print(f"{resource}: ".title() + f"{resources[resource]}")
    elif user_option == "turn off machine":
        machine_in_process = False
        print("See you next time!")
    else:
        if check_resources_available(MENU[user_option]['ingredients'], resources) == False:
            None
        else:
            print(f"\nThe cost is ${MENU[user_option]['cost']}. Please, insert coins.")
            resources = check_money(MENU[user_option], ask_for_money())