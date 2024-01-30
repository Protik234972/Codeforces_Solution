t = int(input())
while t != 0:
    x,n = map(int,input().split())
    mod = x//n
    print(mod)
    t-=1
