def linearSearch(arr,x):
    
    pos = -1
    for index in range(len(arr)):
        if(x==arr[index]):
            pos = index
    return pos+1

if __name__ =="__main__":
    arr = [int(num) for num in input().strip().split(" ")]
    x = int(input())
    index = linearSearch(arr,x)
    print(index)