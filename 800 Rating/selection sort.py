def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        minpos = i
        for j in range(i+1,n):
            if array[j] < array[minpos]:
                minpos = j
        
        temp = array[i]
        array[i]= array[minpos]
        array[minpos]=temp

array=[5, 10, 15, 2, 4, 1, 6]
selection_sort(array)
print(array)
        
                