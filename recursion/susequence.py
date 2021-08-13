
def sub(arr,index,subset):
    if(index==len(arr)):
        if(len(subset)>1):
            subSequence.append([x for x in subset])
        return
    else:
        #select the value at index by add to subset
        subset.append(arr[index])
        sub(arr,index+1,subset)
        #not select the value at index by removing what we add previous
        subset.pop()
        sub(arr,index+1,subset)
def countsub(arr,index,subset=[]):
    if index == len(arr):
        if(len(subset)>1):
            return 1
        return 0
    subset.append(arr[index])
    l = countsub(arr,index+1,subset)
    subset.pop()
    r = countsub(arr,index+1,subset)
    return l+r
arr = [1,2,3,4]
subSequence = []
sub(arr,0,[])
print(subSequence)
count = countsub(arr,0)
print(count)