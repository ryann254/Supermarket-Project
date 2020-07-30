# ABC Supermarket
import random
import os
import json
import datetime
from datetime import date


# Registration
# Helper functions
def is_string(prompt):
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Sorry, you entered the wrong value.\nPlease try again.\n")
            continue
        if len(value) < 3:
            print("Your name has to be atleast 3 characters long.")
            continue
        for char in value:
            if char.isdigit():
                print("Sorry, you entered the wrong value.\nPlease try again.\n")
                continue
        else:
            break
    return value


def is_valid_date(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, you entered the wrong value.\nPlease try again.\n")
            continue
        if 'year' in prompt:
            if len(str(value)) == 4:
                if date.today().year - value < 18:
                    print("You're too young to get a loyalty card.")
                    print('Enjoy your shopping experience at ABC Supermarket')
                    exit()
                elif value < (date.today().year - 150):
                    print("You're too old to get a loyalty card")
                    exit()
            else:
                print("Sorry, you entered the wrong value.\nPlease try again.\n")
                continue

        if 'month' in prompt:
            if value > 12 or value == 0:
                print("Sorry, you entered the wrong value.\nPlease try again.\n")
                continue

        if 'day' in prompt:
            if value > 30 or value == 0:
                print("Sorry, you entered the wrong value.\nPlease try again.\n")
                continue
            else:
                break
        else:
            break
    return value


def is_valid_id_and_telephone(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, you entered the wrong value.\nPlease try again.\n")
            continue
        if 'ID' in prompt:
            if len(str(value)) != 8:
                print("Your ID number needs to be 8 digits long\n")
                continue
        else:
            break
        if 'Telephone' in prompt:
            if len(str(value)) != 9:
                print("Your phone number needs to be atleast 10 digits long\n")
                continue
        else:
            break
    return value

def answers(prompt):
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Sorry, you entered the wrong value.\nPlease try again.\n")
            continue
        if value.lower() == 'yes' or value.lower() == 'y':
            return value
        elif value.lower() == 'no' or value.lower() == 'n':
            return value
        else:
            print("Sorry, you entered the wrong value.\nPlease try again.\n")
            continue

def check_if_birthday(name):
    with open('usersdb.txt', 'r') as file:
        contents = json.load(file)
        for dict in contents:
            if name in dict.values():
                return dict['month'], dict['day']

#Fills the available_compartments db when the program starts
def fill_db():
    compartments = list(range(1, 11))
    with open('available_compartments.txt', 'r+') as file:
        if os.path.getsize('available_compartments.txt') == 0:
            json.dump(compartments, file)

#Assigns an empty compartment number to a customer
def assign_compartment_space(customer):
    if customer == True:
        with open('available_compartments.txt', 'r+') as file:
            contents = json.load(file)
            assign = contents.pop(0)
            file.seek(0)
            file.truncate(0)
            json.dump(contents, file)
            return assign
    elif customer == False:
        with open('usersdb.txt', 'r') as file:
            contents = json.load(file)
            for dict in contents:
                if name in dict.values():
                    compartment = dict['compartment number']
        with open('available_compartments.txt', 'r+') as file:
            contents = json.load(file)
            contents.append(compartment)
            file.seek(0)
            file.truncate(0)
            json.dump(contents, file)

#Add the specific compartment number of every customer to usersdb.txt
def adding_compartment_no(name,compartment,customer):
    if customer == True:
        with open('usersdb.txt', 'r+') as file:
            contents = json.load(file)
            for dict in contents:
                if name in dict.values():
                    dict.update({'compartment number': compartment})
            file.seek(0)
            file.truncate(0)
            json.dump(contents, file)
    elif customer == False:
        with open('usersdb.txt', 'r+') as file:
            contents = json.load(file)
            for dict in contents:
                if name in dict.values():
                    dict.update({'compartment number': compartment})
            file.seek(0)
            file.truncate(0)
            json.dump(contents, file)

def save_user_data():
    with open('usersdb.txt', 'r+') as file:
        if os.path.getsize('usersdb.txt') == 0:
            json.dump(user_data, file)
        else:
            contents = json.load(file)
            contents.append(user_data[0])
            file.seek(0)
            file.truncate(0)
            json.dump(contents,file)

def changing_points(name,points):
    with open('usersdb.txt', 'r+') as file:
        contents = json.load(file)
        for dict in contents:
            if name in dict.values():
                dict.update({'points': points})
        file.seek(0)
        file.truncate(0)
        json.dump(contents, file)

def checking_user_data(name, register):
    if register == False:
        member = False
        with open('usersdb.txt', 'r') as file:
            contents = json.load(file)
            for dict in contents:
                if name in dict.values():
                    print('Welcome back {}.'.format(name))
                    member = True
                    personal_bag(name)

            if member == False:
                print('You\'re not registered with us.\nPlease go and register')
    #Checking if they had already registered before registering them
    else:
        with open('usersdb.txt', 'r') as file:
            contents = json.load(file)
            for dict in contents:
                if name in dict.values():
                    print('Welcome back {}.'.format(name))
                    personal_bag(name)

def checking_available_points(name):
    with open('usersdb.txt', 'r+') as file:
        contents = json.load(file)
        for dict in contents:
            if name in dict.values():
                points_no = dict['points']
        return points_no


def print_final_bill(bill,name,points_gained,birthday,available_points):
    #Removing the set compartment number
    customer = False
    assign_compartment_space(customer)
    compartment = 0
    adding_compartment_no(name,compartment,customer)

    loyalty_points_balance = points_gained + available_points
    changing_points(name,loyalty_points_balance)
    if birthday == True:
        date_time = datetime.datetime.now()
        print("ABC supermarket\n Date and Time: {}\n Hey {}\n Total Amount: {}\n Points Earned: {}\n Points Balance: {}\n Happy BirthDay {}"
              .format(date_time, name, int(bill), int(points_gained), int(loyalty_points_balance), name))
    elif birthday == False:
        date_time = datetime.datetime.now()
        print(
            "ABC supermarket\n Date and Time: {}\n Hey {}\n Total Amount: {}\n Points Earned: {}\n Points Balance: {}\n"
            .format(date_time, name, int(bill), int(points_gained), int(loyalty_points_balance)))
    #For unregistered users
    else:
        date_time = datetime.datetime.now()
        print(
            "ABC supermarket\n Date and Time: {}\n Total Amount: {}\n"
                .format(date_time, int(bill)))

def payment_options(amount):
    if amount > 0:
        value = input('Please indicate how you would like to pay for your goods: [Cash/Mpesa/Visa-card]')
        if value.lower() == 'cash' or value.lower() == 'c':
            return amount
        elif value.lower() == 'mpesa' or value.lower() == 'm' or value.lower() == 'visa-card' or value.lower() == 'v':
            return amount - (amount * 0.02)

def calculating_points(amount):
    if amount >= 5000:
        first_points_gained = 5000/100 * 1
        second_points_gained = (amount - 5000)/100 * 1.5
        return int(float(first_points_gained + second_points_gained))
    else:
        return 0

def calculate_birthday_discount(amount):
    after_discount = amount - (amount * 0.1)
    return after_discount

def requesting_points(name,available_points,amount):
    value = answers('Would you like to redeem your loyalty points: [Yes/no]')
    if value == 'yes' or value == 'y':
        while True:
            try:
                points_no = int(input('You have {} points, how many points would you like to redeem: '
                                      .format(available_points)))
            except ValueError:
                print("Sorry, you entered the wrong value.\nPlease try again.\n")
                continue
            if available_points < points_no:
                print("Sorry, the value you entered is more than your points total.\nPlease try again.\n")
                continue
            if available_points >= points_no:
                remaining_points = available_points - points_no
                changing_points(name,remaining_points)
                bill = amount - points_no
                final_bill = payment_options(bill)
                return final_bill,remaining_points
    elif value == 'no' or value == 'n':
        bill = payment_options(amount)
        return bill,available_points

def done_shopping(name):
    shopping_amount = random.randint(1000, 20000)
    points_gained = calculating_points(shopping_amount)
    current_year = date.today().year
    month,day = check_if_birthday(name)
    birthday = False
    available_points = checking_available_points(name)

    if datetime.date(current_year,month,day) == date.today():
        birthday = True
        after_discount = calculate_birthday_discount(shopping_amount)
        if available_points == 0:
            bill = payment_options(after_discount)
            print_final_bill(bill,name,points_gained,birthday,available_points)
        elif available_points > 0:
            final_bill,remaining_points = requesting_points(name,available_points,after_discount)
            print_final_bill(final_bill,name,points_gained,birthday,remaining_points)
    else:
        if available_points == 0:
            bill = payment_options(shopping_amount)
            print_final_bill(bill,name,points_gained,birthday,available_points)
        elif available_points > 0:
            final_bill,remaining_points = requesting_points(name,available_points,shopping_amount)
            print_final_bill(final_bill,name,points_gained,birthday,remaining_points)


def personal_bag(name):
    value = answers('Do you have a personal bag? [Yes/no]')
    if value == 'yes' or value == 'y':
        customer = True
        compartments_no = assign_compartment_space(customer)
        adding_compartment_no(name,compartments_no,customer)
        print('Your bag has been safely stored in compartment {}'.format(compartments_no))
        done_shopping(name)
    elif value == 'no' or value == 'n':
        done_shopping(name)


# Determines if registration will happen
fill_db()
print('Hello there, Welcome to ABC Supermarket')
customer = answers('Are you registered with our supermarket? [Yes/no]: ')
if customer == 'yes' or customer == 'y':
    register = False
    name = input('Kindly assist us with your name: ')
    checking_user_data(name, register)

elif customer == 'no' or customer == 'n':
    register = True
    confirm = answers('Would you like to register now and earn loyalty points? [Yes/no]: ')
    if confirm == 'yes' or confirm == 'y':
        name = is_string('Please enter your name: ')
        checking_user_data(name, register)
        print("Please enter your date of birth according to the following:")
        year = is_valid_date('Please enter the year: ')
        month = is_valid_date('Please enter the month: ')
        day = is_valid_date('Please enter the day: ')
        dob = datetime.date(year, month, day)
        # id_no = is_valid_id_and_telephone('Please enter your ID number: ')
        # tel_no = is_valid_id_and_telephone('Please enter your Telephone number: ')
        print("Thanks {} for registering with us.\nYour earned loyalty points can be redeemed at any time."
              .format(name))
        user_data = [
            {   'name': name,
                'year': year,
                'month': month,
                'day': day,
                'points': 0
             }
        ]
        save_user_data()
        personal_bag(name)
    else:
        personal_bag()
        print('Enjoy your shopping experience at ABC Supermarket')

# date_entry = input('Please enter your date of birth in this format YYYY-MM-DD: ')
# year, month, day = map(int, date_entry.split('-'))
# dob = datetime.date(year, month, day)
# print(dob)

