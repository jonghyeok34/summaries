from collections import deque

n = 29781
visited = [False] * n


def getCount(start_num):
    if start_num == 1:
        return 0
    queue = deque()
    queue.append([start_num])
    count = 0
    
    divide_numbers = [5,3,2]
    while queue:
        current_numbers = queue.popleft()
        count +=1
        next_numbers = []
        for current_number in current_numbers:
            
            for divide_number in divide_numbers:
                # print(current_number)
                # print(divide_number)
                if current_number % divide_number ==0:
                    new_number = current_number//divide_number
                    if not visited[new_number]:
                        visited[new_number] = True
                        next_numbers.append(new_number)
            if current_number > 1 and not visited[current_number-1]:
                visited[current_number-1] = True
                next_numbers.append(current_number-1)
            
        # if next_number
        reach1 = False
        for check_number in next_numbers:
            if check_number == 1:
                reach1 = True
                break
        if reach1:
            return count
        elif len(next_numbers)>0:
            queue.append(next_numbers)
print(getCount(n))