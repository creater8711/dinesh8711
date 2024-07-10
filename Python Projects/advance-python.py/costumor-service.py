def Hajur_lai_namaskar():
    print("Welcome to the Dinesh Shopping Mall! How may I can help you today?")

def display_our_items():
    items = {
        "1": {"name": "Shoes", "price": 4999},
        "2": {"name": "Shirts", "price": 1499},
        "3": {"name": "Pants", "price": 2199},
        "4": {"name": "Dresses", "price": 3299}
    }
    print("\nAvailable Items:")
    for item_id, item_info in items.items():
        print(f"{item_id}: {item_info['name']} - ${item_info['price']}")

def process_purchase(cart):
    total_cost = 0
    while True:
        choice = input("Enter the item number you want to purchase (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        elif choice in items:
            quantity = int(input("Enter the quantity: "))
            if items[choice]['name'] in cart:
                cart[items[choice]['name']] += quantity
            else:
                cart[items[choice]['name']] = quantity
            total_cost += items[choice]['price'] * quantity
        else:
            print("Invalid item number. Please try again.")
    return total_cost

def calculate_total_cost(total_cost):
    tax_rate = 0.13  
    total_cost_with_tax = total_cost + (total_cost * tax_rate)
    return total_cost_with_tax

def generate_receipt(cart, total_cost_with_tax):
    print("\nReceipt:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")
    print(f"Total cost (including taxes): ${total_cost_with_tax:.2f}")

def Dinesh_shopping_mall():
    cart = {}
    Hajur_lai_namaskar()
    while True:
        print("\nWhat would you like to do?")
        print("1. Display available items")
        print("2. Make a purchase")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_our_items()
        elif choice == '2':
            total_cost = process_purchase(cart)
            total_cost_with_tax = calculate_total_cost(total_cost)
            generate_receipt(cart, total_cost_with_tax)
        elif choice == '3':
            print("\nThank you for visiting the Shopping Mall! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    items = {
        "1": {"name": "Shoes", "price": 4999},
        "2": {"name": "Shirts", "price": 1499},
        "3": {"name": "Pants", "price": 2199},
        "4": {"name": "Dresses", "price": 3299}
    }
    Dinesh_shopping_mall()
