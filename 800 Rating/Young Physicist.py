n = int(input())
temp = 0
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    temp += sum(row)
    matrix.append(row)

if temp != 0:
    print("NO")
    exit()

for j in range(3):
    col_sum = 0
    for k in range(n):
        col_sum += matrix[k][j]
    if col_sum != 0:
        print("NO")
        exit()

print("YES")
