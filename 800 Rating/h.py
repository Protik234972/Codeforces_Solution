
n = int(input())
arr = map(int, input().split())
arr = sorted(arr)
winner = arr[-1]
for i in range(n,-1,-1):
    if winner> arr[i]:
        print(arr[i])
        break
