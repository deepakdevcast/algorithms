def bitSubset(arr):
    subsets = []
    for i in range(1<<len(arr)):
        subset = []
        for bit in range(len(arr)):
            if i & (1<<bit):
                subset.append(arr[bit])
        subsets.append(subset)
    return subsets
arr  =[1,2,3]
subsets = bitSubset(arr)
print(subsets)