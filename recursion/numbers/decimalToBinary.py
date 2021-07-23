def DecimalToBinary(number):
    if number//2==0:
        return number%2
    return str(DecimalToBinary(number//2))+str(number%2)

print(DecimalToBinary(233))