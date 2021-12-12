N, M = map(int, input().split(" "))

coin_count = [float("inf")]* (M+1)
coins = [None] * N
for i in range(N):
    coins[i] = int(input())

coins.sort()
min_coin = coins[0]

for current_total in range(min_coin, M+1):
    for coin in coins:
        if current_total == coin:
            coin_count[current_total] = 1
            break
        elif current_total - coin > 0:
            prev_coin_count = coin_count[current_total- coin]
            if prev_coin_count != float("inf"):
                coin_count[current_total] =  int(min(coin_count[current_total], prev_coin_count +1))

# print(coin_count)
if coin_count[M] == float("inf"):
    print(-1)
else:
    print(coin_count[M])