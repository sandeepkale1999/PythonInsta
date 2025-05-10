

def perCube(n):
    for i in range(n):
        if i*i*i == n:
            return True
        if i*i*i >n:
            return False
    

print(perCube(100))
for i in range(100):
    if perCube(i):
        print(i, end = ' ')
print()       
def perSquare(n):
    for i in range(1,n):
        if i*i == n:
            return True
        if i*i > n:
            return False
        
for j in range(100):
    if perSquare(j):
        print(j, end = ' ')