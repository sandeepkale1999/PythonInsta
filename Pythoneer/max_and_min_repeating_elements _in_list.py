
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4,1,1,1,1,1,1]
# maximun repeating element in the list
print(max(set(test), key = test.count))
# minimun repeating element in the list
print(min(set(test),key = test.count))
