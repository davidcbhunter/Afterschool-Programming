# make a list of favorite games

my_favorite_games = ["The Witcher 3: Wild Hunt", \
                     "Hades",\
                     "Dark Souls III"]

print(my_favorite_games)
print("\n")

#add two games
my_favorite_games.append("Fallout: New Vegas")

my_favorite_games.append("Red Dead Redemption II")

print(my_favorite_games)
print("\n")


#remove one game by name
my_favorite_games.remove("Red Dead Redemption II")
print(my_favorite_games)
print("\n")

#remove one game by order
my_favorite_games.pop(1)
print(my_favorite_games)
print("\n")
