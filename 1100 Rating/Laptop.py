n = int(input())
price = []
quality = []
while n !=0:
    a,b = map(int,input().split())
    price.append(a)
    quality.append(b)
    n-=1
if price.index(min(price)) ==  quality.index(max(price)):
    print("Happy Alex")
else:
    print("Poor Alex")