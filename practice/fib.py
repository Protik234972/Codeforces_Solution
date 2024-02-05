def fib(n,memo = {}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        memo[n]=fib(n-1,memo) + fib(n-2,memo)
        return memo[n]
print(fib(0))
print(fib(10))
print(fib(50))