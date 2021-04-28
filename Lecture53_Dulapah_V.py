def vatCalculate(totalPrice):
    result = totalPrice + ((totalPrice * 7) / 100)
    return result

print(vatCalculate(int(input("Enter Total Price : "))))