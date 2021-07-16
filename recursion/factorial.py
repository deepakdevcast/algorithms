def fact(n):
    if n<0:
        return -1
    elif n==0:
        return 1
    elif n<=2:
        return n
    else:
        return n*fact(n-1)

if __name__== "__main__":
    result = fact(int(input("Enter number: ")))
    if result == -1:
        print("invalid value")
    else:
        print(result)