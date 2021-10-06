fruits = {"apple", "banana", "pineapple", "orange"}
print(fruits)
fruits.remove("banana")
fruits.add("grape")
print(fruits)

userInput = int(input("Enter Number of Your Favorite Fruits : "))
myFruits = set()
while len(myFruits) < userInput:
    myFruits.add(input("Fruits : "))
    print(myFruits)