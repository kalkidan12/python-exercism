def is_armstrong_number(number):
    numstr = str(number) # ['1, '2]
    num = list(numstr)
    l = len(num)
    sum = 0
    for i in num:
        sum +=int(i)**l
    if sum == number:
        return True
    return False
    
print(is_armstrong_number(9474))   
