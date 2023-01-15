# Name: Oby Bkkourh
# Project's name: Find recent addresses
# Date: 1/15/2023

# This function takes a list of tuples, where each tuple contains an address
# string and a date string in this format: "L3, 20 queen road,1992" from the user input
# which is in the following while loop

def most_recent_date(addresses_and_dates):
    most_recent_dates = {}
    for address, date_str in addresses_and_dates:
        date = date_str
        if address in most_recent_dates:
            if date > most_recent_dates[address]:
                most_recent_dates[address] = date
        else:
            most_recent_dates[address] = date
    return most_recent_dates


addresses_and_dates = []

# This loop is meant to take user input and then put it in a tuple and then separate
# commas to find the required values
# or if user input is "done" show results
while True:
    input_str = input("Enter an address and date in the format 'address,YYYY-MM-DD' or 'done' to finish: ")
    if input_str.strip().lower() == 'done':
        break
    else:
        TheIn = tuple(input_str.split(",")[1:])
        addresses_and_dates.append(TheIn)

# this is meant to call the function and print the results out.
print(most_recent_date(addresses_and_dates))
