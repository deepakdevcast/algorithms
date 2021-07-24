def mergetwoarr(arr1,arr2,arr3=[]):
    if len(arr1)==0:
        for i in arr2:
            arr3.append(i)
        return arr3
    if len(arr2)==0: 
        for i in arr1:
            arr3.append(i)
        return arr3
    if arr1[0]<arr2[0]:
        arr3.append(arr1[0])
        mergetwoarr(arr1[1:],arr2,arr3)
        return arr3
    else:
        arr3.append(arr2[0])
        mergetwoarr(arr1,arr2[1:],arr3)
        return arr3

arr1= [10,21,32,41,50]
arr2 = [2,12,20,21,32,60,100]
arr3= mergetwoarr(arr1,arr2)
print(arr3)