from typing import List

class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        """Initialize an empty shopping cart."""
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        """Add a single item to the cart."""
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        """Return the number of items currently in the cart."""
        return len(self.items)

    def get_items(self) -> List[str]:
        """Return a list of all items in the cart."""
        return self.items

    def get_total_price(self, price_map):
        """Calculate the total price of items in the cart using the given price map."""
        pass