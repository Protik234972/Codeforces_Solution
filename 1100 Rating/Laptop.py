n = int(input())
while n !=0:
    a,b = map(int, input().split())
    if a>b:
        print("Happy Alex")
        exit()
    n-=1
print("Poor Alex")
