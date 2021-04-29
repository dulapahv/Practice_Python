menuList = []
priceList = []


def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])


def findTotal():
    total = 0
    for i in range(len(priceList)):
        total += int(priceList[i])
    print("Total", total)


while True:
    menuName = input("Please Enter Menu Name : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
findTotal()
