
a = 9
b = 6 
x = 0

while x < 100:
    x += a 
    while b < a:
        print(x,a,b)
        if x%b == 0:
            print('yes')
            break
        b += b
        print('y')
    print('t')
    
print(5%int(1e9+7))

    
v = list(map(int,input().split()))
v.sort()
print((v[0] * (v[1] - 1) * (v[2] - 2)) % int(1e9+7))
