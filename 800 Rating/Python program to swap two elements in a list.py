list = [23,65,19,90]
pos1,pos2 = map(int,input().split())
temp = list[pos1-1]
list[pos1-1] = list[pos2-1]
list[pos2-1] = temp

print(list)