def calculate_total(price, quantity):
    return price * quantity

assert calculate_total(10, 2) == 20
assert calculate_total(0, 5) == 0
print(f"${calculate_total(19.99, 3):.2f}")
