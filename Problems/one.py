print('sandeep kale')

queries = int(input())
dic = dict.fromkeys(range(queries),0)

for i in range(queries):
    dic[i] = [int(i) for i in input().split(' ')]

for k in dic.values():
    if k[0]*k[1] > k[2]:
        pass
    if k[0]*k[1] < k[2]:
        print('multiplication of {} and {} with bound {} not possible'.format(k[0],k[1],k[2]))


