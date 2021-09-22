def fibDP(n,mapping):
    if mapping[n-1]!=0:
        return mapping[n-1]
    if n==2:
        return 1
    elif n<2:
        return n
    mapping[n-1] = fibDP(n-1,mapping)+fibDP(n-2,mapping)
    return mapping[n-1]

n=int(input())
hashed = [0 for i in range(n)]
value=fibDP(n,hashed)
print(value)
