# Programmer: Ivan van der Merwe
# Date: 24 November 2018
# Purpose: Tip Calculator - takes input of user and returns tip amount

def reservation():
    customers = input('Reservation for how many people: ')
    while int(customers) < 0:
        reservation()
    print(f'\nYour reservation is for {customers} people.\n') 

reservation()

def calculate_tip():
    # Request bill amount 
    bill = input('Please enter your bill amount: ')
    print(f'\nYour bill is: R{bill}\

    # Request tip percentage
    tip_percentage = input('Tip percentage: ')
    print(f'\nYour tip percentage is: {tip_percentage}%\n')

    # Tip percentage
    converted_tip = int(tip_percentage) / 100

    tip = int(bill) * converted_tip
    print(f'The tip amount is R{tip}')

    # bill including tip
    total = bill + tip
    print(f"Your total is {total}")

calculate_tip()