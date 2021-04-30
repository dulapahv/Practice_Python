systemMenu = {"ข้าวหมกไก่": 45, "ข้าวมันไก่": 40, "ข้าวมันไก่ผสม": 50, "ข้าวมันไก่พิดศษ": 45}
menuList = []


def showBill():
    total = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += menuList[number][1]
    print("Total", total)

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()