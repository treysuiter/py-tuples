zoo = ("cat", "giraffe", "viper", "panther", "muppet", "roach", "monitor lizard", "Julian", "goat", "donkey")

print(zoo.index("Julian"))

animal_to_find = "Julian"

if animal_to_find in zoo:
    print("Animal was found")
else:
    print("Animal was not found")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)

zoo = list(zoo)

print("zoo list", zoo)

zoo.extend(["badger", "bat", "falcon"])

zoo = tuple(zoo)

print("tuple zoo 2", zoo)