# Programmer: Ivan van der Merwe
# Date: 24 November 2018
# Purpose: Tip Calculator - takes input of user and returns tip amount

reserved = 0

# Request valid input for amount of customers
def reservation():
    while True:
        try:
            global reserved
            reserved = int(input('How many people is the table for: '))
            break
        except:
            print('Invalid input please enter a number')
reservation()   

if reserved == 0:
    print('You did not make a reservation, please make a reservation')
    reservation()
else:
    print(f'\nYour reservation is for {reserved} people.\n')

def calculate_tip():
    # Request bill amount 
    bill = input('Please enter your bill amount: ')
    print(f'\nYour bill is: R{bill}')

    # Request tip percentage
    tip_percentage = input('Tip percentage: ')
    print(f'\nYour tip percentage is: {tip_percentage}%\n')

    # Tip percentage
    converted_tip = int(tip_percentage) / 100

    tip = int(bill) * converted_tip
    print(f'The tip amount is R{tip}')

    # bill including tip
    total = int(bill) + int(tip)
    print(f"Your total is {total}")

calculate_tip()

