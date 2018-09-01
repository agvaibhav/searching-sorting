"""
intepolation position formula:
pos = lo + [ (x - arr[lo])*(hi-lo)/(arr[hi]-arr[lo]) ]
"""

def interpolSearch(arr,lo,hi, x):

    while lo<=hi and x>=arr[lo] and x<=arr[hi]:
        
        pos = lo + int( (x - arr[lo])*(hi-lo)/(arr[hi]-arr[lo]) )

        if arr[pos]==x:
            return pos

        elif arr[pos]>x:
            hi = pos-1

        elif arr[pos]<x:
            lo = pos+1
        

    return -1


arr = [10,20,30,40,50,60,70,80]
x=20
result = interpolSearch(arr,0,len(arr)-1,x)
if result==-1:
    print("element is not present in array")

else:
    print("element is found at index {}".format(result))
