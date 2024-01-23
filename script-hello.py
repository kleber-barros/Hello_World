name = input("What is your name? ")
while any(char.isdigit() for char in name):
    print("Invalid format. Please enter a valid name.")
    name = input("What is your name? ")
print("Hello World, " + name)
