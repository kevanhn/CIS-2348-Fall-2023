# Kevin Nguyen 1928145

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Prompt the user for the first item
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # Prompt the user for the second item
    print("\nItem 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # Calculate and print the total cost
    total_cost = item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${total_cost}")
