def revArr(arr,pointer=0):
    if(pointer==len(arr)//2):
        return arr
    else:
        arr[pointer],arr[len(arr)-1-pointer] = arr[len(arr)-1-pointer],arr[pointer]
        return revArr(arr,pointer+1)
revarr = revArr([10,20,30,40])
print(revarr)