original_string = "hello"
s = input()
i = 0
for j in s:
    if  original_string[i] == j:
        i +=1
if i == 4:
    print("YES")
else:
    print("NO")