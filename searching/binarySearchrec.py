def binarySearchrec(arr,left,right,x):
    if(left<=right):
        mid = (left+right) // 2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            right = mid-1
            return binarySearchrec(arr,left,mid-1,x)
        elif(arr[mid]<x):
            left = mid+1
            return binarySearchrec(arr,mid+1,right,x)
    return None

if __name__ == "__main__":
    # arr = [int(num) for num in input().strip().split(" ")]
    arr = [1,2,3,4,5,6,7,8,9]
    # x = int(input())
    x=7
    index = binarySearchrec(arr,0,len(arr)-1,x)
    print(index+1)