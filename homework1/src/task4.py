"Caroline Duncan, 2/12/26, calculates and returns the final price of an item after applying a percentage discount "
def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price
