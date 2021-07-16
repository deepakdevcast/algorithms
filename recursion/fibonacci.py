def fibonacci(n):
    if n<0:
        return fibonacci(n+2)-fibonacci(n+1)
    elif n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

result = fibonacci(int(input()))
print(result)