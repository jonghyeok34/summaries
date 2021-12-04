
inputStr ="A01CD234SDSA56ASASC78KOQEWP9"

alphabetRange = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numberRange = "0123456789"
def main():
    alphabetOnlyStr=""
    numberSum = 0
    print(inputStr)
    for char in inputStr:
        if char in alphabetRange:
            alphabetOnlyStr+=char
        if char in numberRange:
            numberSum += int(char)
    
    result ="".join(sorted(alphabetOnlyStr)) + str(numberSum)
    print(result)


main()