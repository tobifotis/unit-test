# 🛒 Shopping Cart 

A simple, test-driven shopping cart system built in Python.  
Supports item limits and total price calculation using an external item database.

## Features
- Add items to the cart
- Enforce maximum cart size
- Calculate total price via injected price source (mockable)
- Unit tested with `pytest` and `unittest.mock`

## Requirements
- colorama==0.4.6
- iniconfig==2.1.0
- packaging==25.0
- pluggy==1.6.0
- Pygments==2.19.2
- pytest==8.4.1

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

## Project Structure
```
shopping_cart.py       # ShoppingCart class logic
item_database.py       # Price lookup interface
test_shopping_cart.py  # Unit tests using pytest and mocking
```

---

## License
This project is open-source under the [MIT License](LICENSE).
