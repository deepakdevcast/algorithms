def reversestr(str,i):
    if i==len(str):
        return ""
    return reversestr(str,i+1) + str[i]

print(reversestr("Deepak",0))