n, k = map(int, input().split())

s = 240 - k
problems_solved = 0

for i in range(1, n + 1):
    s -= i * 5
    print(s)
    problems_solved += 1
    if s < 0:
        print(problems_solved -1)
        break
else:
    print(problems_solved)
