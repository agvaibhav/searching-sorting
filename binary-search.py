def binarySearch(arr, lower_index, upper_index, x):
    if upper_index>=0:
        mid = lower_index+((upper_index - lower_index)//2)
        if arr[mid]==x:
            
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, 0, mid-1, x)
        elif arr[mid]<x:
            return binarySearch(arr, mid+1, len(arr)-1, x)
    else:
        return -1

arr = [1,2,3,4,5,6]
x=5
result = binarySearch(arr, 0 , len(arr)-1, x)
if result==-1:
    print("element is not found in array")
else:
    print("element found at index {}".format(result))
