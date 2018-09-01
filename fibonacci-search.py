def fibSearch(arr, n, x):

    fib2=0
    fib1=1
    fib = fib1+fib2

    while(fib<n):
        fib2=fib1
        fib1=fib
        fib = fib1+fib2

    offset =0

    while(fib>1):
        i = min(offset+fib2, n-1)
        if arr[i]<x:
            fib=fib1
            fib1=fib2
            fib2=fib-fib1
            offset = i

        elif arr[i]>x:
            fib = fib2
            fib1 = fib1-fib2
            fib2 = fib-fib1

        else:
            return i

    if(fib1 and arr[offset] == x):
        return offset

    return -1
arr=[2]
#arr = [1,2,3,4,5,6,7,8]
x=2
n=len(arr)
result = fibSearch(arr, n , x)
if result == -1:
    print("element is not present in array")
else:
    print("element is found at index {}".format(result))
