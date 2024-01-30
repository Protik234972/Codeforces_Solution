list = [12, 13, 14, 15]
new_list=[]
for i in list:
    count =0
    for j in str(i):
        count+=int(j)
    new_list.append(count)
print(new_list)
    