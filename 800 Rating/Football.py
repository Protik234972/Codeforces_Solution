n = int(input())
goal = 0

while n > 0:
    if goal != 0:
        team = input()
        if team == win:
            goal += 1
        else:
            goal -= 1
    else:
        win = input()
        goal = 1

    n -= 1

print(win)
