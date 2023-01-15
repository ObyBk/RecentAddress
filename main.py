
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
while True:
    input_str = input("Enter an address and date in the format 'address,YYYY-MM-DD' or 'done' to finish: ")
    if input_str.strip().lower() == 'done':
        break
    else:
        TheIn = tuple(input_str.split(",")[1:])
        addresses_and_dates.append(TheIn)





print(most_recent_date(addresses_and_dates))

