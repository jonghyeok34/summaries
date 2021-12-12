# N = row count , M = column count
N =3
M = 4
max_values = []
gold_map = [
    [1,3,3,2],
    [2,1,4,1],
    [0,6,4,7]
]
move_commands = [(0, 1), (1,1), (-1,1)]

# for move_command in move_commands:
#    print(move_command[0])

for i in range(N):
    max_values.append([0]*M)
    max_values[i][0] = gold_map[i][0]

for j in range(M-1):
   for i in range(N):
        # move command 실행하여
        # 입력된 것과, 새로 나온 값중큰 것으로 
        for move_command in move_commands:
            if 0<= i+ move_command[0] <N:
                next_row = i+ move_command[0]
                next_col = j+ move_command[1]
                next_max_value = max_values[next_row][next_col]
                expected_max_value = max_values[i][j] + gold_map[next_row][next_col]
                max_values[next_row][next_col] =  max(expected_max_value , next_max_value)

result_max = 0
for i in range(N):
    result_max = max(result_max, max_values[i][M-1])
print(result_max)