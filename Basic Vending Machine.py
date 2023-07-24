product_one = "orange juice"
product_one_price = 150
product_one_amount = 15

product_two = "black coffee"
product_two_price = 120
product_two_amount = 30

product_three = "Milk Tea"
product_three_price = 130
product_three_amount = 30

product_four = "Dr. Pepper"
product_four_price = 150
product_four_amount = 20

product_five = "Monster"
product_five_price = 220
product_five_amount = 25


choice = ""

def show_products():
    print(product_one + "\t" + product_two + "\t" + product_three + "\t" + \
          product_four + "\t" + \
          product_five)
    print(str(product_one_price) + "\t" + str(product_two_price) + "\t" + \
          str(product_three_price) + "\t" + str(product_four_price) + "\t" + \
          str(product_five_price))

while choice != "q":
    show_products()
    #choice will be the product number: 1, 2, 3, etc
    choice = input("Please pick a product.\n")
