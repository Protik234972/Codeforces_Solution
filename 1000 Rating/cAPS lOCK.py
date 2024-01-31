s = input()
flag = True

for i in range(1,len(s)):
    if s[i].islower():
        flag = False
  
if flag != True:
    print(s)
elif flag == True and s[0].isupper():
    print(s.lower())
else:
    print(s.title())