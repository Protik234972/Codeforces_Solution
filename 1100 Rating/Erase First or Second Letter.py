t = int(input())
while t != 0:
    n = int(input())
    s = input()
    my_set = set()
    ans = 0
    
    for i in s:
        my_set.add(i)
        ans+=len(my_set)
    
    t -= 1
    print(ans)