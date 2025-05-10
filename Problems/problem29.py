
'''deloitte problem 
eg. input = 3011 output = 3**1
    input = 4122 output = 4**12
    input = 2021 output = 20**2'''
num = 3011
def main(num):

    str_num = str(num)
    last = int(str_num[-1])
    str_num2 = str_num[:-1]
    rev_str_num2 = str_num2[::-1]
    rev_power_str = rev_str_num2[0:last]
    power = int(rev_power_str[::-1])

    base = int(str_num[0:len(str_num)-last-1])
    
    print(base, power)

    return base**power 
    
    
arr = [4122,2021]
sum = 0
for num in arr:
    sum += main(num)
    
print(sum)