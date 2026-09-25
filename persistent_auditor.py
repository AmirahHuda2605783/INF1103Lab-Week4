def load_inventory():
    orders = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) == 3:
                    order_id = parts[0].strip()
                    product_name = parts[1].strip()
                    quantity = int(parts[2].strip())

                    orders.append([order_id, product_name, quantity])

    except FileNotFoundError:
        orders = []

    except (ValueError, OSError):
        orders = []

    return orders


def save_inventory(orders, history):
    with open("inventory.txt", "w") as file:
        for order in orders:
            file.write(
                order[0] + ", " +
                order[1] + ", " +
                str(order[2]) + "\n"
            )

        file.write("\nTransaction History:\n")

        for transaction in history:
            file.write(str(transaction) + "\n")


def display_orders(orders):
    print("Current Orders:")
    print()

    for order in orders:
        print(
            order[0] + ", " +
            order[1] + ", " +
            str(order[2])
        )

    print()


def get_next_order_id(orders):
    if len(orders) == 0:
        return 1001

    highest_id = 1000

    for order in orders:
        try:
            order_id = int(order[0])

            if order_id > highest_id:
                highest_id = order_id

        except ValueError:
            continue

    return highest_id + 1


def get_quantity():
    while True:
        quantity = input("Enter Quantity: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print("Invalid quantity. Please enter a positive whole number.")


def main():
    orders = load_inventory()
    history = []

    display_orders(orders)

    product_name = input("Enter Product Name: ").strip()

    while product_name == "":
        print("Product name cannot be empty.")
        product_name = input("Enter Product Name: ").strip()

    quantity = get_quantity()

    order_id = get_next_order_id(orders)

    new_order = [
        str(order_id),
        product_name,
        quantity
    ]

    orders.append(new_order)

    history.append(quantity)

    print()
    print("New Order Added: ")
    print(
        str(order_id) + ", " +
        product_name + ", " +
        str(quantity)
    )
    print()

    save_inventory(orders, history)

    print("Order successfully saved to inventory.txt")


if __name__ == "__main__":
    main()