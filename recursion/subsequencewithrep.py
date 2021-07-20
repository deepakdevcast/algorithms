def subrep(arr,subset,index,sum):
    if sum==0:
        subSequence.append([x for x in subset]) 
        return
    if index==len(arr):
        if sum==0:
            subSequence.append([x for x in subset]) 
        return
    if arr[index]<=sum:
        subset.append(arr[index])
        sum = sum-arr[index]
        subrep(arr,subset,index,sum)
        subset.pop()
        sum +=arr[index]
    subrep(arr,subset,index+1,sum)

def countsub(arr,index,sum):
    if sum==0: return 1
    if index==len(arr):
        if sum==0:
            return 1
        return 0
    l=0
    if sum>=arr[index]:
        l = countsub(arr,index,sum-arr[index])
    r= countsub(arr,index+1,sum)
    return l+r

arr=[1,2,3,4]
subSequence = []
subrep(arr,[],0,7)
print(subSequence)
print(countsub(arr,0,7))