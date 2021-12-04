
numStr = "1234567890"
plusNum = (0,1)

numbers = []
for numChar in numStr:
    numbers.append(int(numChar))
print(numbers)

prevNum = 0
totalNum = 0
for number in numbers:
    if prevNum <=1 or number <=1:
        totalNum += number
    else:
        totalNum *= number
    prevNum = number

print(totalNum)

