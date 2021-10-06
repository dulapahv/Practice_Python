def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Wrong Username or Password! Please Try Again.")
        return login()


def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. exit")
    return menuSelect()


def menuSelect():
    userSelected = int(input("What would you like to do? "))
    if userSelected == 1:
        pricevat = int(input("Input Total Price : "))
        print("Total Price (VAT 7% Included) is", vatCalculator(pricevat), "THB")
        return menuSelect()
    elif userSelected == 2:
        print("Total Price (VAT 7% Included) is", priceCalculator(), "THB")
    elif userSelected == 3:
        return exit()
    else:
        print("Please select available actions!")
        return menuSelect()


def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    sum = price1 + price2
    print("Total Price (VAT 7% NOT Included", sum)
    return vatCalculator(price1 + price2)


login()