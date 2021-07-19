#condition is sum of subset is divisible by 5
def sub(arr,index,subset,sum=0):
    if(index==len(arr)):
        if sum%5==0:
            subSequence.append([x for x in subset])
        return
    else:
        #select the value at index by add to subset
        subset.append(arr[index])
        sum += arr[index]
        sub(arr,index+1,subset,sum)
        #not select the value at index by removing what we add previous
        subset.pop()
        sum += arr[index]
        sub(arr,index+1,subset,sum)

def countsub(arr,index,sum):
    if index == len(arr):
        if sum%5==0:
            return 1
        return 0
    sum += arr[index]
    l = countsub(arr,index+1,sum)
    sum -= arr[index] 
    r = countsub(arr,index+1,sum)
    return l+r
arr = [1,2,3,4]
subSequence = []
sub(arr,0,[])
print(subSequence)
count = countsub(arr,0,0)
print(count)