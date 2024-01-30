def IsPrime(num):
    flag = True
    for i in range(2, (num//2) +1):
        if num%i ==0:
            flag = False
            return flag
    return flag
    
print(IsPrime(4))