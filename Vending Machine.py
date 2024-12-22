from prettytable import PrettyTable

#Self to note, this one will use functions, as they serve as reusable blocks of code.
#A nested dictionary, with 4 sub-nested dictionaries is used here to store 2 key pairs, the first is the item, and the second, price, in a 2 decimal place format.
menu = {
    'Drinks': {
        'A01': {'item': 'Soda', 'price': 1.50},
        'A02': {'item': 'Juice', 'price': 2.05},
        'A03': {'item': 'Water', 'price': 1.00},
        'A04': {'item': 'Cola', 'price': 1.40},
    },
    'Chips': {
        'B01': {'item': 'Doritos', 'price': 0.50},
        'B02': {'item': 'Cheetos', 'price': 1.15},
        'B03': {'item': 'Nachos', 'price': 1.05},
        'B04': {'item': 'Chips', 'price': 2.00}
    },
    'Candy':{ 
        'C01': {'item': 'Lollipop', 'price': 1.35},
        'C02': {'item': 'Chocolate bar', 'price': 0.45},
        'C03': {'item': 'Gummy bears', 'price': 1.45},
        'C04': {'item': 'Skittles', 'price': 0.25},
    },
    'Cookies':{
        'D01': {'item': 'Oreo', 'price': 1.25},
        'D02': {'item': 'Crackers', 'price': 0.55},
        'D03': {'item': 'Chips ahoy', 'price': 1.55},
        'D04': {'item': 'Shortbread', 'price': 0.75},
    }
}


print("Distributeur automatique") #When the programs runs, a title will be displayed, using a print statment.

def Show_menu():
    table = PrettyTable()
    table.field_names = ["Code", "Item", "Price", "Category"]  # Adding a new column for category
    
    for category, items in menu.items():
        for code, details in items.items():
            table.add_row([code, details['item'], f"${details['price']:.2f}", category])  # Adding the category to the row

def obtain_user_choice():  # A function used to let the user choose what they're buying.
    while True:
        Choice = input("Enter the code of your choosing: ")  # Asks the user to input any one of the codes from the menu.
        if Choice in [code for category in menu.values() for code in category]:  # Check if the choice is valid
            return Choice  # If the option is valid, it'll return the code of choice.
        else:
            print("Invalid, try again.")  # If the option is invalid, it'll send an acknowledgment to the user and tell them to try again.

def handle_payment(price): #A function to(as the name implies) handle the payment, that is if the user has enough money.
    while True:
        try:
            money_inserted = float(input(f"Insert ${price:.2f}: ")) #Will ask the user to insert required amount. 
            if money_inserted >= price:
                change = money_inserted - price #If any money is remaining, return change, via sbutraction of the 
                return change
            else:
                print(f"Insufficient funds. You need ${price - money_inserted:.2f} more.") #If the user doesn't have enough money, the user is informed of the shortfall.
        except ValueError:
            print("Invalid.") #In the event if the input wasn't valid.

def dispense_item(item, price, change):
    print(f"Dispensing {item}...")
    if change > 0:
        print(f"Your change is: ${change:.2f}") #If there is change, the user will be notified.
    else:
        print("You have no change remaining.") #Same goes if there is no change.


def vending_machine():  # A function, comprised of 4 sub-functions, all working in unison.
    while True:
        Show_menu()  # Shows the user the menu.
        selection = obtain_user_choice()  # Gets the user's choice
        
        for category, items in menu.items():  # Find the item and price using the selection code
            if selection in items:
                item = items[selection]['item']
                price = items[selection]['price']
                break
        
        change = handle_payment(price)  
        dispense_item(item, price, change)   
        
        another = input("Do you want to buy another item? (y/n): ").lower()  # Asks the user if they want to buy another item.
        if another != 'y':
            print("Thank you for using the Vending Machine!")
            break  # Exits the loop, thus ending the utility app.


vending_machine() #Calling out the function, runs the program, as it is a function, comprised of 4 funcitons. 