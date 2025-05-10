# given legs and heads of rabits and chickens find how many rabits and chickens
legs = 200
heads = 72

for i in range(heads+1):
    r = i
    c = heads - i
    if 4 * r + 2 * c == 200:
        print(r,c)


# r = no of rabbits
# c = no of chickens 
