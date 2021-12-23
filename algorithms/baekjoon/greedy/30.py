numbers = [int(x) for x in input()]
# 30의 배수
# 10의 자리가 3,6,9,2,5,8,1,4 중 하나
# 숫자개수 10^5
possible_first_non_zeros = [3,6,9]
possible_first_non_zeros_2 = [12,15,18,21,24,27]
# 10의 자리가 0일때 가능한 100의 자리
# 2자리
numberLen = len(numbers)
result = "-1"

def number_list_to_string(numbers:list):
    result = ""
    for number in numbers:
        result += str(number)
    return result
        
numbers.sort(reverse=True)
if 0<=numberLen<1:
    result = "-1"
if numbers[-1] != 0:
    result = "-1"
elif numberLen == 2:
    if numbers[0] in possible_first_non_zeros and numbers[1] ==0:
        result = number_list_to_string(numbers=numbers)      
elif numberLen >= 3:
    first_non_zero_index = -1
    lastZeroIndex = 1
    # last zero from list
    for i in range(2, numberLen+1):
        current_number = numbers[-i]
        if current_number == 0:
            lastZeroIndex =i
        if lastZeroIndex != i:
            # print(current_number, lastZeroIndex, i)
            first_non_zero_index = i
            break
    # first non zero & compare to possible numbers
    if numbers[first_non_zero_index] not in possible_first_non_zeros:
        comparing_index = -1
        for i in range(first_non_zero_index+1, numberLen+1):
            if numbers[first_non_zero_index] != numbers[i]:
                comparing_index = i
                break
        # if it is not possible number find possible number and switch by index
        if comparing_index == -1:
            result = "-1"
        else:
            temp_num = numbers[first_non_zero_index]
            numbers[first_non_zero_index] = numbers[comparing_index] 
            numbers[comparing_index] = temp_num
            result = number_list_to_string(numbers=numbers)
        
    else:
        result = number_list_to_string(numbers=numbers)
            
    
# 3자리 이상

print(int(result))