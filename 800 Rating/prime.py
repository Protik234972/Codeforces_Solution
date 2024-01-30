def isPrimeSlow(num):
    divisionCounter = 0
    if num <=1 :return False, divisionCounter
    
    for i in range(2, num):
        divisionCounter +=1
        if num % i == 0: return False ,divisionCounter
    return True, divisionCounter

print(isPrimeSlow(9))
print(isPrimeSlow(1))
print(isPrimeSlow(3))
print(isPrimeSlow(2))
print(isPrimeSlow(11))
