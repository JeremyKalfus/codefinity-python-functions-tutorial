prices = [210, 0, -891, 432, 256]

apply_tax = lambda x: max(x, 0) * (1-0.13)   # Deducting 13% tax

final_prices = [apply_tax(i) for i in prices]

# Testing the result
print(final_prices)