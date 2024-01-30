def is_prime_partially_optimized(num):
    c = 0
    if num <=1: return False, c
    
    for i in range(2, num//2 +1):
        c +=1
        if num%i ==0:return False, c
    return True, c
print(is_prime_partially_optimized(9))
print(is_prime_partially_optimized(1))
print(is_prime_partially_optimized(3))
print(is_prime_partially_optimized(2))
print(is_prime_partially_optimized(11))