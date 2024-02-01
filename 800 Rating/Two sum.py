nums, target = map(int, input().split())
a = list(map(int, input().split()))
position_dict = {}

for i in range(nums):
    complement = target - a[i]
    if complement in position_dict:
        print(position_dict[complement] + 1, i + 1)
        break
    position_dict[a[i]] = i

else:
    print(-1)
