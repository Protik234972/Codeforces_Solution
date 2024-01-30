def binary_search(arry,target):
    low = 0
    high = len(arry)-1
    while low <= high:
        mid = (low+high)//2
        if arry[mid] == target:
            print("Found")
            return
        elif arry[mid]<target:
            low = arry[mid+1]
        elif arry[mid] > target:
            high = arry[mid-1]
        else:
            print("Not found")
arry =[1,2,3,4,5,6,7,8,9,10]
binary_search(arry,15)