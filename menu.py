menu = ["tea", "coffee", "soup", "sandwich", "biscuit", "cake"]
# menu list created with 6 items
stock = {
    "tea": 35,
    "coffee": 40,
    "soup": 15,
    "sandwich": 16,
    "biscuit": 20,
    "cake": 6
}
# dictionary for stock
price = {
    "tea": 2.90,
    "coffee": 3.80,
    "soup": 5.00,
    "sandwich": 6.00,
    "biscuit": 3.00,
    "cake": 4.00
}
# dictionary for prices
total = 0
for item in menu:
    item_value = stock[item]*price[item]
    total += item_value
    # total is each individual items worth added
print("Total value of stock: £ {:.2f}".format(total))
# value to 2 d.p.