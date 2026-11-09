MAX_NUMBERS_ORDERED = 20


class Cart:
    """Shopping cart that holds up to MAX_NUMBERS_ORDERED DVDs."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        """Add a DVD to the cart. Returns True on success, False if full."""
        if len(self.items) > MAX_NUMBERS_ORDERED:
            print("The cart is almost full.")
            return False
        self.items.append(dvd)
        print(f"The disc has been added.")
        return True

    def remove_dvd(self, dvd):
        """Remove a DVD from the cart."""
        if dvd in self.items:
            self.items.remove(dvd)
            print(f"The disc has been removed.")

    def total_cost(self):
        """Calculate total cost of all DVDs in cart."""
        return sum(dvd.cost for dvd in self.items)
