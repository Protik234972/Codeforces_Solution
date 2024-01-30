def powerSum(X, N):
    # write your code here
    def count_ways(target, num):
        if target == 0:
            return 1
        if target < 0 or num <= 0:
            return 0
        
        ways_without_current = count_ways(target, num - 1)
        ways_with_current = count_ways(target - num ** N, num - 1)
        
        return ways_without_current + ways_with_current
    
    return count_ways(X, int(X ** (1/N)))

print(powerSum(13,2))