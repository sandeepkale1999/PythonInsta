
n = 4
triplets = [(i,j,k) for i in range(1,n+1) for j in range(i,n+1) for k in range(j,n+1) if i*j*k <=n]
print(triplets)
print(len(triplets))

def main(a,b,n):
    ad = int(str(a),n)
    bd = int(str(b),n)
    print(ad+bd)
    
    
main(1011,10100,2)
main(7,8,9)