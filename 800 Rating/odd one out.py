t= int(input())
while t !=0:
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif a == c :
        print(b)
    else:
        print(a)

    t-=1