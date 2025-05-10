# longest working slot
''' longest working slot
    Given an array containing arrays of empId and clock time.
    Consider emp at index 0 started from t = 0
    emp 1 time = 3 hrs
    emp 1 time = 5-3 = 2 hrs
    Find which employee have done work for max time without break
    {0: 4, 2: 2, 1: 6}
'''

arr = [[0,3],[2,5],[0,9],[1,15]]

dic = {}
for ep in arr:
    dic[ep[0]] = 0
    
dic[arr[0][0]] = arr[0][1]

i = 1
j = 0

while i < len(arr):
    if dic[arr[i][0]] < (arr[i][1] - arr[j][1]):
        dic[arr[i][0]] = (arr[i][1] - arr[j][1])
    i += 1
    j += 1
               
print(dic)


def getKey(dic, val):
    for k,v in dic.items():
        if v == val:
            return k
        
print(getKey(dic, max(dic.values())))




    
