def NaturalSum(number):
    if number==1:
        return number
    return number + NaturalSum(number-1)

print(NaturalSum(10))