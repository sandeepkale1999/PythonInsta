 
 
def perfectCube(N):
    cube = 0
    for i in range(N+1):
        cube = i*i*i
        if cube == N:
            return True
        elif cube > N:
            return False
        
print(perfectCube(121))
print(perfectCube(216))

        
def perfectSquare(n):
    root = n**0.5
    if int(root) == root:
        return True
    else:
        return False
    
print(perfectSquare(4))
print(perfectSquare(3))