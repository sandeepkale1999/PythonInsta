
# Flatening of a list 
global final
final = []
def flatenList(arr):
    for ele in arr:
        if type(ele) == list:
            flatenList(ele)
        else:
            final.append(ele)
      
    
arr = [1,2,3,[4,5,[6],7],8]
flatenList(arr)
print(final)
