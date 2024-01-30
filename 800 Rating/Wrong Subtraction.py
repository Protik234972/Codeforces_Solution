n , k = map(int, input().split())

while k != 0:
    re = n % 10
    if re != 0:
        n = n -1
    else:
        n = n//10
    k-=1
print(n)
