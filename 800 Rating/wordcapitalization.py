
def string():
    s = input()
    s_new = ' '

    for i in range(0,len(s)):
        if i==0:
            s_new += s[i].upper()
        else:
            s_new +=s[i]
    print(s_new)
    
string()