import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    products_dict = read_dictionary("products.csv", 0)
    print("All Products")
    print(products_dict)

    print("Requested Items")

    with open("request.csv", "r") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row in reader:
            product_number = row[0]
            quantity = int(row[1])

            if product_number in products_dict:
                product = products_dict[product_number]
                name = product[1]
                price = product[2]
                print(f"{name}: {quantity} @ {price}")
            else:
                print(f"Product {product_number} not found in product list.")

if __name__ == "__main__":
    main()
