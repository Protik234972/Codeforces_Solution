original_string = "hello"
s = input()
i = 0

for j in s:
    if i < len(original_string) and original_string[i] == j:
        i += 1

if i == len(original_string):
    print("YES")
else:
    print("NO")
