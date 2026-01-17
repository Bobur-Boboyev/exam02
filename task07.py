def calculate_cart(cart: dict) -> int:
    total_price = sum(
        list(
            map(
                lambda x: x[1]['price'] * x[1]['quantity'],
                cart.items()
            )
        )
    )
    return total_price

cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
print(calculate_cart(cart))