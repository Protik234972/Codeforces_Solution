def construct_array(n):
    if n % 4 != 0:
        return "NO"
    array = []
    half = n//2
    print("YES")
    for i in range(1,half +1):
        array.append(2*i)

    for i in range(half -1):
        array.append(array[i] -1)
    array.append(array[half -1] + half -1)

    return array

    




