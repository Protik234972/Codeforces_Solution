def cumulative(A):
    for i in range(1, len(A)):
        A[i] = A[i] + A[i-1]
    print(A)
A= [2,5,2,1,4]
cumulative(A)