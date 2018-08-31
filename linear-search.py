def linearSearch(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):  
            return i
    return -1

arr=[20,45,12,89,75]
x=89
result = linearSearch(arr,x)

if result==-1:
    print("element does not match in given array")
else:
    print("element is found at index {}".format(result))
