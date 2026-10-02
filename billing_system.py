
#   Mini Project (W3): Billing System (OOP-based)

class Product:
    """Represents a single product with name, price, and quantity."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        """Returns price * quantity for this product."""
        return self.price * self.quantity


class Bill:
    """Represents a customer's bill containing multiple products."""

    def __init__(self, tax_rate):
        self.products = []       # list of Product objects
        self.tax_rate = tax_rate # tax rate as a decimal (e.g. 0.18 for 18%)

    def add_product(self, product):
        """Add a Product object to the bill."""
        self.products.append(product)

    def total_before_tax(self):
        """Sum of all product subtotals."""
        return sum(p.subtotal() for p in self.products)

    def tax_amount(self):
        """Tax calculated on the subtotal."""
        return self.total_before_tax() * self.tax_rate

    def grand_total(self):
        """Subtotal + tax."""
        return self.total_before_tax() + self.tax_amount()

    def display_bill(self):
        """Print the full bill in a tabular format."""
        width = 51
        tax_label = f"Tax ({self.tax_rate * 100:.1f}%):"

        print("=" * width)
        print("BILLING RECEIPT".center(width))
        print("=" * width)
        print(f"{'No.':<5} {'Product':<15} {'Price':>8} {'Qty':>5} {'Amount':>10}")
        print("-" * width)

        for i, p in enumerate(self.products, start=1):
            print(f"{i:<5} {p.name:<15} {p.price:>8.2f} {p.quantity:>5} {p.subtotal():>10.2f}")

        print("-" * width)
        print(f"{'Subtotal:':>{width - 10}} {self.total_before_tax():>9.2f}")
        print(f"{tax_label:>{width - 10}} {self.tax_amount():>9.2f}")
        print(f"{'Grand Total:':>{width - 10}} {self.grand_total():>9.2f}")
        print("=" * width)

#   Main Program

def main():
    print("=" * 40)
    print("      WELCOME TO THE BILLING SYSTEM")
    print("=" * 40)

    # --- Tax rate input ---
    while True:
        try:
            tax_input = float(input("\nEnter tax rate (in %): "))
            if tax_input < 0:
                print("Tax rate cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number (e.g. 18 for 18%).")

    bill = Bill(tax_rate=tax_input / 100)

    # --- Number of products ---
    while True:
        try:
            n = int(input("\nHow many products do you want to add? "))
            if n <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(1, n + 1):
        print(f"\n--- Product {i} ---")

        name = input("  Product name   : ").strip()
        while not name:
            print("  Name cannot be empty.")
            name = input("  Product name   : ").strip()

        while True:
            try:
                price = float(input("  Price per unit : "))
                if price < 0:
                    print("  Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("  Invalid price. Enter a number (e.g. 25.50).")

        while True:
            try:
                quantity = int(input("  Quantity       : "))
                if quantity <= 0:
                    print("  Quantity must be at least 1.")
                    continue
                break
            except ValueError:
                print("  Invalid quantity. Enter a whole number.")

        bill.add_product(Product(name, price, quantity))
        print(f"  ✔ '{name}' added.")

    print()
    bill.display_bill()


if __name__ == "__main__":
    main()
