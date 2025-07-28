import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

items = [
    {"name": "bolt M8x50", "quantity": 50, "unit":"pcs", "unit_price":"1.00"},
    {"name": "bolt M8x100", "quantity": 150, "unit":"pcs", "unit_price":"1.50"},
    {"name": "bolt M8x150", "quantity": 550, "unit":"pcs", "unit_price":"2.00"},
]

def get_items(items):
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print(50 * "=")
    for item in items:
        name = item["name"]
        quantity = item["quantity"]
        unit = item["unit"]
        unit_price = float(item["unit_price"])
        print(f"{name}\t{quantity}\t{unit}\t{unit_price}")


if __name__ == "__main__":
    print("Magazyn")
    while True:
        todo = input("What would you like to do? ")

        if todo == "exit":
            logging.info("Exiting... Bye!")
            break
        if todo == "show":
            get_items(items)