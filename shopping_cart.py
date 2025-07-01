from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: List[str] = []

    def add(self, item: str):
        """Add a single item to the cart."""
        self.items.append(item)

    def size(self) -> int:
        """Return the number of items currently in the cart."""
        return len(self.items)

    def get_items(self) -> List[str]:
        """Return a list of all items in the cart."""
        pass

    def get_total_price(self, price_map):
        """Calculate the total price of items in the cart using the given price map."""
        pass