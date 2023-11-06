# Kevin Nguyen 1928145

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for x in self.cart_items:
            if x.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for x in self.cart_items:
            if x.item_name == modified_item.item_name:
                x.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for x in self.cart_items:
            total_quantity += x.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for x in self.cart_items:
            total_cost += x.item_quantity * x.item_price
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        for x in self.cart_items:
            x.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for x in self.cart_items:
            x.print_item_description()


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    print(menu)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    user_input = input()
    if user_input != 'q':
        print_menu(cart)

    flag = True
    while flag:
        choice = input("Choose an option:\n")
        if choice == 'a':
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(modified_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            flag = False
        else:
            choice = input("Choose an option:\n")
