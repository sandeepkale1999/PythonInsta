# accolite mustafa's code

def hunt(p,c,n,m):
    pr = p[::-1]
    cr = c[::-1]

    costs = []
    for row in pr:
        cs = []
        if pr.index(row) == 0:
            costs.append(row)
        else:
            idx = 0
            for k in row:
                cs.append(abs(k-cr[pr.index(row)][idx]))
                idx += 1
            costs.append(cs)           
    s = 0 
    for r in costs:
        s += min(r) 
    return s
                            
n = 3
m = 3
p = [[3,2,5],
    [8,9,1],
    [4,7,6]]

c = [[1,1,1],
    [1,1,1],
    [1,1,1]]
       
print(hunt(p,c,n,m))

        