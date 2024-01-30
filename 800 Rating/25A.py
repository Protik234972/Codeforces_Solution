def evenness(li):
    even_count = 0
    odd_count = 0
    even = 0
    odd = 0
    for i in li:
        if i % 2 == 0:
            even_count += 1
            even += i
        else:
            odd_count += 1
            odd += i
 
    if even_count == 1:
        for i in range(len(li)):
            if li[i] == even:
                return i+1
 
    else:
        for i in range(len(li)):
            if li[i] == odd:
                return i+1
 
n = int(input())
li = []
while n > 0:
    s = int(input())
    li.append(s)
    n -= 1
print(evenness(li))
