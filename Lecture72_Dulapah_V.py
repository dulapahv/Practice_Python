menuList = []
total = []


def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number])
    print("Total", sum(total))


while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])
        total.append(menuPrice)
showBill()
