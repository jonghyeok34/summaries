# LIS 가장 긴 증가하는 부분 수열 이용
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식 이용하기

# 입력 받은 병사 정보 뒤집은 이후 LIS 적용

n = int(input())
array = list(map(int, input().split()))
array.reverse()

print(array)
dp = [1]* n
print(dp)
for i in range(1, n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] +1)
# print(dp)
# 열외 병사 최소 수
print(n - max(dp))