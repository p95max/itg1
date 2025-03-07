# Shop_Simulator

import time

text = ""

products = {

    "Bananas": 35,
    "Apples ": 20,
    "Potato": 10,
    "Watermelon": 50

}

buyer_bal = 100

print("Your current balance =  " + str(buyer_bal) + "$")

lines = text.strip().split("\n")
for line in lines:
    print(line)                                                                                                 # Timer1
    time.sleep(2)

print("Products list:")
for product, price in products.items():
    print(f"Product: {product}, Price: {price} $")

lines = text.strip().split("\n")
for line in lines:
    print(line)                                                                                                 # Timer2
    time.sleep(2)

# Quantity of products in Cart logic

cart = {}
prices = {}                                                                                              #Product_prices
total_sum = 0                                                                                      #Total_products_summe


def add_to_cart(product, quantity, price):
    global total_sum

    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity
        prices[product] = price

    total_sum += price * quantity
    #save prod sum
    print(f"Product {product} added to your cart in quantity {quantity} Price: {price} per item")


while True:
    product = input("Enter product name (or enter 'exit' to quit): ")
    if product.lower() == 'exit':                                                              #if products not choosed
        break
    try:
        if product in products:
            price = products[product]
            quantity = int(input(f"Enter quantity for {product}: "))
            add_to_cart(product, quantity, price)
    except ValueError:
        print("Please enter a valid number for price and quantity.")

print("Your cart:", cart)
for product, quantity in cart.items():
    print(f"Product: {product}, Quantity: {quantity} items x {prices[product]} $ = {prices[product] * quantity} $")
    print(f"Total sum: {total_sum} $")