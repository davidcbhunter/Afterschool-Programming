#product_one = "orange juice"
#product_one_price = 150
#product_one_amount = 15

#product_two = "black coffee"
#product_two_price = 120
#product_two_amount = 30

#product_three = "Milk Tea"
#product_three_price = 130
#product_three_amount = 30

#product_four = "Dr. Pepper"
#product_four_price = 150
#product_four_amount = 20

#product_five = "Monster"
#product_five_price = 220
#product_five_amount = 25

product_list = ["Orange Juice", "Black Coffee",\
                "Milk Tea", "Dr. Pepper", \
                "Monster"]

product_price_list = [150,120,130,150,220]

product_amount_list = [15,30,30,20,25]

choice = ""
money_in_vending_machine = 1000

def show_products():
    message = ""
    for p in product_list:
        message += p + "\t"
    print(message)
    print(str(product_one_price) + "\t" + str(product_two_price) + "\t" + \
          str(product_three_price) + "\t" + str(product_four_price) + "\t" + \
          str(product_five_price))

def is_product():
    return choice == 1 or choice == 2 or \
           choice == 3 or choice == 4 or \
           choice == 5

def is_sold_out():
    return (choice == 1 and product_one_amount == 0) or\
           (choice == 2 and product_two_amount == 0) or\
           (choice == 3 and product_three_amount == 0) or\
           (choice == 4 and product_four_amount == 0) or\
           (choice == 5 and product_five_amount == 0)

def is_enough_money():
    return (choice == 1 and product_one_price <= money) or\
           (choice == 2 and product_two_price <= money) or\
           (choice == 3 and product_three_price <= money) or\
           (choice == 4 and product_four_price <= money) or\
           (choice == 5 and product_five_price <= money)

def buy(mivm):
    global product_one_amount
    global product_two_amount
    global product_three_amount
    global product_four_amount
    global product_five_amount
    if choice == 1:
        product_one_amount -= 1
        mivm += product_one_price
        change = money - product_one_price
        print("You have " + str(change) + " yen in change.")
        print("Enjoy your " + product_one)
    elif choice == 2:
        product_two_amount -= 1
        mivm += product_two_price
        change = money - product_two_price
        print("You have " + str(change) + " yen in change.")
        print("Enjoy your " + product_two)
    elif choice == 3:
        product_three_amount -= 1
        mivm += product_three_price
        change = money - product_three_price
        print("You have " + str(change) + " yen in change.")
        print("Enjoy your " + product_three)
    elif choice == 4:
        product_four_amount -= 1
        mivm += product_four_price
        change = money - product_four_price
        print("You have " + str(change) + " yen in change.")
        print("Enjoy your " + product_four)
    else:
        product_five_amount -= 1
        mivm += product_five_price
        change = money - product_five_price
        print("You have " + str(change) + " yen in change.")
        print("Enjoy your " + product_five)

while choice != "q":
    show_products()
    #choice will be the product number: 1, 2, 3, etc
    choice = input("Please pick a product.\n")
    #print(type(choice))
    if choice.isnumeric():
        choice = int(choice)
    #check if choice is OK
        if is_product():
            print(str(choice) + " was chosen.\n")
            #check if the product is in stock
            if is_sold_out():
                print("Sold out.\n")
            else:
                money = input("Please enter money.\n")
                if money.isnumeric():
                    #print("safe!")
                    #convert the money to an int
                    money = int(money)
                    #check if it is enough money
                    if is_enough_money():
                        #print("enough")
                        #buy the product
                        buy(money_in_vending_machine)
                    else:
                        print("Not enough money\n")
        else:
            print("Sorry. Pick again.\n")
    else:
        print("Sorry. Pick again.\n")
    
