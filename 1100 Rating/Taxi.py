n = int(input())
frequency = [0, 0, 0, 0]
total = 0

students = map(int, input().split())
for i in students:
    frequency[i-1] += 1

total = frequency[3] + frequency[2] + frequency[1] // 2
frequency[0] -= frequency[2]

if frequency[1] % 2 == 1:
    total += 1
    frequency[0] -= 2

if frequency[0] > 0:
    if frequency[0] <= 4:
        total += 1
    elif frequency[0] % 4 == 0:
        total += frequency[0] // 4
    else:
        total += (frequency[0] // 4) + 1

print(total)
