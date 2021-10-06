tupleExample = ('Nono', 'Mickey', 'Gram')
print(tupleExample)
tupleExample2 = ('Putter', 'Nick', 'Omo')
tupleExample3 = tupleExample + (tupleExample2 * 2)
print(tupleExample3)
print(tupleExample3[:2])
print('Yeen' in tupleExample3)


for i in tupleExample3:
    print("hello", i)