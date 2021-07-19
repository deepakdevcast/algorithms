
def sub(arr,index,subset):
    if(index==len(arr)):
        subSequence.append([x for x in subset])
        return
    else:
        #select the value at index by add to subset
        subset.append(arr[index])
        sub(arr,index+1,subset)
        #not select the value at index by removing what we add previous
        subset.pop()
        sub(arr,index+1,subset)
def countsub(arr,index):
    if index == len(arr):
        return 1
    l = countsub(arr,index+1)
    r = countsub(arr,index+1)
    return l+r
arr = [1,2,3,4]
subSequence = []
sub(arr,0,[])
print(subSequence)
count = countsub(arr,0)
print(count)