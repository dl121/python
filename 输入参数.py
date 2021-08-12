months = (0,31,59,90,120,151,181,212,243,273,304,334)

year = int(input('输入年:\n'))

while True:
    month = int(input('输入月:\n'))
    if month in range(1,13):
        break
    else:
        print('The month is NOT in 1 to 12')

day = int(input('输入日:\n'))

sum = months[month-1] + day

if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if(month > 2):
        sum += 1

print(sum)