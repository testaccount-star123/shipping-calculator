shipping.py:

def shipping_cost(weight_kg, express=False):
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    base = 4.0 if weight_kg <= 1 else 4.0 + 1.5 * (weight_kg - 1)
    return round(base * (1.8 if express else 1.0), 2)
