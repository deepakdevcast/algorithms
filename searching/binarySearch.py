def binarySearch(arr,x):
    pos = -1
    left = 0
    right = len(arr)-1
    while(left<=right):
        mid = (left+right) // 2
        if(arr[mid]==x):
            pos = mid
            return pos
        elif(arr[mid]>x):
            right = mid-1
        elif(arr[mid]<x):
            left = mid+1
    return None

if __name__ == "__main__":
    # arr = [int(num) for num in input().strip().split(" ")]
    arr = [1,2,3,4,5,6,7,8,9]
    # x = int(input())
    x=7
    index = binarySearch(arr,x)
    print(index)