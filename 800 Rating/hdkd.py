def isPrime(n, i=2, count = 0):
    
    # for if condition
    count +=1
    if n == i:
        count+=1
        return True, count
    elif n % i == 0:
        count+=1
        return False, count
    count +=1
    return isPrime(n, i + 1 , count)
n = 971
if isPrime(n,2):
    print("Yes,", n, "is Prime")
else:
    print("No,", n, "is not a Prime")