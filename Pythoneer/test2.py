import datetime
import calendar

def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, int(n**0.5), 2):
                if n%i == 0:
                    return False
            return True
   
days = ['Sun', 'Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat']
def findDay(year, month, day):
    dt = datetime.date(year,month,day)
    return dt.strftime('%A')[:3]
    
    
inp = '20211202 Wed 100'
y,m,d = int(inp[:4]), int(inp[4:6]), int(inp[6:8]),

d2 = inp.split()[-2]
n = int(inp.split()[-1])

day = findDay(y,m,d)
print(day)

print(d+abs(days.index(d2)-days.index(day)))


While True:
    



 
