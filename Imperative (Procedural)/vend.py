class Vend:
    def __init__(self):
        self.products = {"Water": 1.00, "Soda": 1.50, "Cola": 1.25, "Chocolate": 1.75}

    def display_products(self):
        print("Available products:")
        for product, price in self.products.items():
            print(f"{product} - ${price}")

    def buy_product(self, product, money):
        if product not in self.products:
            print("Invalid product selection.")
            return

        price = self.products[product]
        if money < price:
            print("Insufficient funds. Please insert more money.")
            return

        change = money - price
        print(f"You bought {product}.")
        if change > 0:
            print(f"Your change is: ${change:.2f}")

    def start(self):
        print("Welcome to the Vending Machine!")
        while True:
            self.display_products()
            print("Enter the product you want to buy (or 'exit' to exit):")
            product = input().capitalize()
            if product == 'Exit':
                print("Thank you for using the vending machine. Goodbye!")
                break
            if product not in self.products:
                print("Invalid product selection.")
                continue
            print("Enter the amount of money:")
            money = float(input())
            self.buy_product(product, money)


if __name__ == "__main__":
    vending_machine = Vend()
    vending_machine.start()
