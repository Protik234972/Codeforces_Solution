def compareTriplets(a,b):
    a_count = 0
    b_count = 0
    for i in range(3):
        if a[i] > b[i]:
            a_count +=1
        elif a[i] < b[i]:
            b_count +=1
    return [a_count , b_count]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(compareTriplets(a,b))