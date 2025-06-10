# Added code to calculate and print a reminder 
# showing how many days are left until the New Year's Sale

import csv
from datetime import datetime

PRODUCTS_FILENAME = "products.csv"
REQUEST_FILENAME = "request.csv"
SALES_TAX_RATE = 0.06

def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit(1)
    return dictionary

def main():
    products_dict = read_dictionary(PRODUCTS_FILENAME, 0)

    total_items = 0
    subtotal = 0

    print("Inkom Emporium")

    try:
        with open(REQUEST_FILENAME, "r") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                try:
                    product = products_dict[product_number]
                    name = product[1]
                    price = float(product[2])
                    print(f"{name}: {quantity} @ {price:.2f}")
                    total_items += quantity
                    subtotal += price * quantity
                except KeyError as e:
                    print("Error: unknown product ID in the request.csv file")
                    print(e)
                    exit(1)
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit(1)

    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at the Inkom Emporium.")

    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %e %H:%M:%S %Y"))

    today = current_date_and_time.date()
    next_new_year = datetime(year=today.year + 1, month=1, day=1).date()
    days_until_new_year = (next_new_year - today).days

    print(f"Only {days_until_new_year} day(s) until our New Year's Sale!")

if __name__ == "__main__":
    main()