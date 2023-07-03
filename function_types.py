def greet():
    print("Hi, Mei and Yuna!")

def greet_two(name_one,name_two):
    print("Hi, " + name_one + " and " + name_two)


def greet_three():
    return "Hi, Yuna and Mei"

def greet_four(name_one, name_two):
    return "Hi, " + name_one + " and " + name_two

message = greet_four("Momoka","Mio")

print(message)

#add, no return
def add(num_one,num_two):
    print(num_one+num_two)

#add, return
def add_two(num_one,num_two):
    return num_one+num_two

answer = add_two(1234134,13451234)

