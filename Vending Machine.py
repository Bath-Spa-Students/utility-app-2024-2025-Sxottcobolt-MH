#Self to note, this one will use functions, as they serve as reusable blocks of code.
#A nested dictionary is used here to store 2 key pairs, the first is the item, and the second, price, in a 2 decimal place format.
menu = {
    '0': {'item': 'Soda', 'price': 1.50},
    '1': {'item': 'Nachos', 'price': 1.05},
    '2': {'item': 'Candy', 'price': 0.50},
    '3': {'item': 'Oreo', 'price': 1.15},
    '4': {'item': 'Juice', 'price': 2.05},
    '5': {'item': 'Water', 'price': 1.00},
    '6': {'item': 'Chips', 'price': 2.00}
}

print("Distributeur automatique") #When the programs runs, a title will be displayed, using a print statment.

def Show_menu(): #A function to show the user what's available in the vending machine.
   print("Our menu:")
   for code, details in menu.items(): #To iterate over each item in the menu, displaying code, name, and price each item.
      print(f"Code {code}: {details['item']}-${details['price']:.2f}") #The :.2f is a format specifier, used to format float values by 2 places.

def obtain_user_choice(): #A function used to let the user choose what they're buying.
   while True:
      Choice = input("Enter the code of your choosing: ") #Asks the user to input 1 out of the 6 codes from the menu.
      if Choice in menu:
        return Choice #If the option is valid, it'll return the code of choice.
      else:
         print("Invalid, try again.") #If the option is invalid, it'll send an acknowledgement to the user, and tell them to do it again.

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
        print(f"Your change is: ${change:.2f}") #If there is change, the user will be nortified.
    else:
        print("You have no change remaining.") #Same goes if there is no change.


def vending_machine(): #A function, comprised of 4 sub-functions, all wroking in unison.
    while True:
        Show_menu()  #Shows the user the menu.
        selection = obtain_user_choice() #Gets the user's choice
        item = menu[selection]['item'] #Display the item the user selected, and the price.
        price = menu[selection]['price']
        
        change = handle_payment(price)  
        dispense_item(item, price, change)   
        another = input("Do you want to buy another item? (y/n): ").lower() #Asks the user if they want to buy another item.
        if another != 'y':
            print("Thank you for using the Vending Machine!")
            break #Exits the loop, but also ending the utility app.

vending_machine() #Calling out the function, runs the program, as it is a function, comprised of 4 funcitons. 