def palindrome(str,i):
    if i==len(str)//2:
        return True
    if str[i]==str[len(str)-1-i]:
        return palindrome(str,i+1)
    return False

print(palindrome("kabk",0))