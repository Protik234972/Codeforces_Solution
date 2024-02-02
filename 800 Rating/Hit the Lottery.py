def minimum_bills(n):
    denominations = [100, 20, 10, 5, 1]
    count = 0

    for denomination in denominations:
        count += n // denomination
        n %= denomination

    return count

# Read input
n = int(input())

# Output result
result = minimum_bills(n)
print(result)
