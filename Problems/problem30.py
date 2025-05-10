'''Deloitte problem ## incomplete solution.. 
    Given an array of baskets capacity 
    customer wants to buy N apples
    Find number of ways in which apple can be packed with given baskets.'''
     
baskets = [15,20,17,45,11]
apples = 55
count = 0
for basket in baskets:
    if apples%basket == 0:
        count += 1
# for other combinations 
y = 0
while y <= len(baskets):
    start = 0
    end = 2+y
    while end <= len(baskets):
        s = sum(baskets[start:end])
        if s == apples:
            count += 1
        else:
            pass
        start += 1 
        end += 1 
    y += 1
    
# number of possible ways to fill the apples with given basket size 
print(count)
