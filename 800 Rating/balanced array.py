t = int(input())

while t!=0:
    n = int(input())

    if (n//2) % 2 == 0:
        print("YES")
        m = n//2
        for i in range(m):
            print((2+2*i),end=" ")
        for j in range(m-1):
            print((1+2*j),end=" ")
        print((2+2*i)+ (m-1))
        
    else:
        print("NO")
    t-=1     
    
    
    