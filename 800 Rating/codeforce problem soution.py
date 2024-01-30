def string():
    s = input().lower()
    v = 'aieyou'
    new_s = ''
    for char in s:
        if char not in v:
            new_s += '.' + char
            
    print(new_s)

string()

        