for x in range(12):
    break
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))

for val in "hello":
    if val == "l":
        continue # When continue, the loop will continue without processing below function.
    print(val)

print("The end")

