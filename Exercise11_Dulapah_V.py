number = int(input("Floor : "))
for i in range(number):
    print(" " * (number - i), "*" * ((2 * i) + 1))