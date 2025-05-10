



def ArrayChallange(strArr):
    arr = strArr
    set1 = set([int(i) for i in arr[0].split(',')])
    set2 = set([int(j) for j in arr[1].split(',')])
    arr2 = list(set1.intersection(set2))
    return ','.join([str(i) for i in arr2])






arr = ['1,3,4,7,13','1,2,4,13,15']
print(ArrayChallange(arr))


names = ['sandeep','kale']

print(','.join(names))

print(' '.join(names))

nums = [1,2,3,4,5]
nums = [str(i) for i in nums]
print('-'.join(nums))