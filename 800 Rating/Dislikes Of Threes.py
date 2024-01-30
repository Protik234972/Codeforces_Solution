array = [0] * 1001
j = 1
for i in range(1,1667):
    if i % 3 != 0 and i % 10 != 3:
        array[j] = i
        j+=1
n = int(input())
while n != 0:
    num = int(input())
    print(array[num])
    n-=1
