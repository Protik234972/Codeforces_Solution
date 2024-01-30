import math
def optimized_is_prime(num):
    counter = 0
    if num <= 1: return False, counter
    
    for i in range(2,int(math.sqrt(num)) +1):
        counter +=1
        if num % i == 0: return False, counter
    return True, counter
print(optimized_is_prime(9))
print(optimized_is_prime(1))
print(optimized_is_prime(3))
print(optimized_is_prime(2))
print(optimized_is_prime(11))