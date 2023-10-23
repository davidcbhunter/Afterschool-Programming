my_family = ["Kathy","Doug","Michael","David",\
             "Mark","Sarah","Rachel"]

print(my_family[0])
my_family[0] = "Katherine"
print(my_family[0])


if "Tom" in my_family:
    print("Hi, Tom!")

if "Doug" in my_family:
    print("Hi, Doug!")


print(len(my_family))

for f in my_family:
    print(f)

second_year_classes = [31,29,30,31,25]

print(type(second_year_classes))

#print(second_year_classes[-1])

print(second_year_classes)
second_year_classes.insert(1,20)
print(second_year_classes)

second_year_classes.append(27)
print(second_year_classes)

second_year_classes.remove(20)
print(second_year_classes)


second_year_classes.pop(4)
print(second_year_classes)
