n,m,a,b = map(int,input().split())
 
if m *a < b :
    print(n*a)
else:
    cost = ((n//m) * b) + min((n%m)*a,b)
    print(cost)