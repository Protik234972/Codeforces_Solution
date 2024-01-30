def calculate_bit(res, b):
    if b == "++X" or b == "X++":
        res += 1
    elif b == "--X" or b == "X--":
        res -= 1
    return res

n = int(input())
res = 0

while 0 < n:
    b = input()
    res = calculate_bit(res, b)
    n -= 1

print(res)
