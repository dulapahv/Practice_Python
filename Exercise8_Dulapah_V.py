username = input("Username : ")
password = input("Password : ")
if username == "n0miya" and password == "02468":
    print("===Welcome to Animate shop!===")
    print("We sell the following items!")
    print("1. Anime Figure  1500 THB")
    print("2. Anime Poster  3000 THB")
    print("3. Anime MV CD   2000 THB")
    print("Please select the items you like to purchase.")
    product1 = int(input("Item : "))
    quantity1 = int(input("Quantity : "))
    total1 = 0
    total2 = 0
    total3 = 0
    if product1 == 1:
        total1 += 1500
    elif product1 == 2:
        total1 += 3000
    elif product1 == 3:
        total1 += 2000
    else:
        print("Please select only items that are available!")
    total1 *= quantity1
    print("Do you want to buy anything else?")
    answer1 = str(input("Y/N"))
    if answer1 == "Y" or answer1 == "y":
        product2 = int(input("Item : "))
        quantity2 = int(input("Quantity : "))
        if product2 == 1:
            total2 += 1500
        elif product2 == 2:
            total2 += 3000
        elif product2 == 3:
            total2 += 2000
        else:
            print("Please select only items that are available!")
        total2 *= quantity2
    if answer1 == "N" or answer1 == "n":
        print("Total :", total1)
        exit(1)
    print("Do you want to buy anything else?")
    answer2 = str(input("Y/N"))
    if answer2 == "Y" or answer2 == "y":
        product3 = int(input("Item : "))
        quantity3 = int(input("Quantity : "))
        if product3 == 1:
            total3 += 1500
        elif product3 == 2:
            total3 += 3000
        elif product3 == 3:
            total3 += 2000
        else:
            print("Please select only items that are available!")
        total3 *= quantity3
        print("Total :", total1 + total2 + total3)
        exit(1)
    if answer2 == "N" or answer2 == "n":
        print("Total :", total1 + total2)
        exit(1)
else:
    print("Wrong Username or Password!")