file = open("basic.txt", "w")
file.write("Hello Python Programming...!")
file.close()

with open("basic.txt", "w") as file:
    file.write("Hello Python Programming...!")
    