import math
def jumpSearch(arr, n, x):
    step =int(math.sqrt(n))
    i = 1
    while(arr[int((min(i,n))-1)]<=x):
        j = min(i,n)-1

        if arr[j]==x:
            return j

        prev = j
        i=i+step

        if prev >= n-1:
            return -1
        
    j = min(i, n)-1
    if arr[j]>x:
            upper_index = j
            lower_index = prev
            return binarySearch(arr,lower_index, upper_index, x)
    
        
    else:
        return -1

def binarySearch(arr, lower_index, upper_index, x):
    if upper_index >=0:
        mid = lower_index + ((upper_index-lower_index)//2)
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, lower-index, mid-1, x)
        elif arr[mid]<x:
            return binarySearch(arr, mid+1, upper_index, x)
    else:
        return -1

arr=[1,2,3,4,5,6]
x = 6
result = jumpSearch(arr,len(arr), x)
if result==-1:
    print("element is not present in array")
else:
    print("element is found at index {}".format(result))
