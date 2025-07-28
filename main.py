import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

if __name__ == "__main__":
    print("Magazyn")
    while True:
        todo = input("What would you like to do? ")

        if todo == "exit":
            logging.info("Exiting... Bye!")
            break