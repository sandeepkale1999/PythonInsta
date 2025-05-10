
def hcf(a,b):  
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            hcf = i
            return hcf
        
print(hcf(12,17))

def lcm(a,b):
    mx = max(a,b)
    mul = 1
    hc = 1
    while True:
        if hc%a == 0 and hc%b == 0:
            return hc
        hc = mul*mx
        mul += 1

print(lcm(12,6))
print(lcm(17,7))



