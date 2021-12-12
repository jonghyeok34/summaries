# N명 특정 전투력
# 높은 병사 앞 - 내림차순(항상)
# 배치 시 -  특정 위치 열외, 남아 있는 병사 최대로
# N =  전사 수
N = 7

soldiers = [15, 11, 4, 8, 5,2,4]
is_omitted = [False]*N
omitted_count = 0
for i in range(1, len(soldiers)):
    # check previous
    for j in range(1, i):
        check_index = i-j
        if soldiers[check_index]< soldiers[i]:
            # print(i, j)
            if not is_omitted[check_index]:
                is_omitted[check_index] = True
                omitted_count +=1
        else:
            break

# print(is_omitted)
print(omitted_count)
