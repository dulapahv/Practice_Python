price = int(input("Price : "))
if price < 0:
    print("Please input positive integer!")
    exit(1)
vat = int(input("vat : "))
result = price + ((price * vat) / 100)
print(result)
