N, M = map(int, input().split(" "))

coins = [None] * N
for i in range(N):
    coins[i] = int(input())

coins.sort()

# DP 테이블초기화
coin_count = [float("inf")]* (M+1)
coin_count[0] = 0

for coin_order in range(N):
    for j in range(coins[coin_order], M+1):
        if coin_count[j-coins[coin_order]] !=float("inf"):
            coin_count[j] = min(coin_count[j], coin_count[j -coins[coin_order]] +1)

# 계산된 결과 출력 
if coin_count[M] == float("inf"):
    print(-1)
else:
    print(coin_count[M])