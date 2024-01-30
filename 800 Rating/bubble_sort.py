def sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1]=temp
    
array=[5,10,15,2,4,1,6]
print(array)
sort(array)
print(array)
             