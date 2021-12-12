# N = row count , M = column count
for tc in range(int(input())):
    N , M = map(int, input().split())
    index = 0
    gold_map = list(map(int, input().split()))
    max_values = []
    move_commands = [(0, 1), (1,1), (-1,1)]
    index = 0
    for i in range(N):
        max_values.append(gold_map[index:index+M])
        index += M
    
    
    for j in range(1, M):
        for i in range(N):
            # move command 실행하여
            # 입력된 것과, 새로 나온 값중큰 것으로 
            for move_command in move_commands:
                if i ==0 : left_up = 0
                else: left_up = max_values[i-1][j-1]
                if i == N-1: left_down = 0
                else: left_down = max_values[i+1][j-1]
                left = max_values[i][j-1]
                max_values[i][j] = max_values[i][j] +max(left_up, left, left_down)
    result_max = 0
    for i in range(N):
        result_max = max(result_max, max_values[i][M-1])
    print(result_max)