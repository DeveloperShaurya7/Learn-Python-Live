class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"{name} added to cart at price {price}.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from cart.")
        else:
            print(f"{name} not found in cart.")
    
    def calculate_total(self):
        total = sum(self.items.values())
        print(f"Total price: {total}")
        return total
    
    def apply_discount(self, discount):
        total = self.calculate_total()
        discounted_total = total * (1 - discount)
        print(f"Total after {discount*100}% discount: {discounted_total}")
        return discounted_total
    

cart = ShoppingCart()
cart.add_item("Laptop", 120000)
cart.add_item("Headphones", 2000)
cart.calculate_total()
cart.apply_discount(0.1)
cart.remove_item("Headphones")
cart.calculate_total()