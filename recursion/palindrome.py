def checkPalindrome(word,pointer=0):
    if pointer == len(word)//2:
        return True
    else:
        if word[pointer]== word[len(word) -1 - pointer]:
            return checkPalindrome(word,pointer+1)
        else:
            return False

check = checkPalindrome("ass")
print(check)