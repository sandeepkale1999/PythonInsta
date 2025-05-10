
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4,1,1,1,1,1,1]
print(max(set(test), key = test.count))

print(min(set(test),key = test.count))