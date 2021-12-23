N, k =map(int, input().split(" ",2))
a = []
for i in range(N):
    a.append(int(input()))

count = 0
for j in range(1, N+1):
    coin = a[-j]
    if k % coin < k:
        this_count = k // coin
        k -= coin* this_count
        count += this_count
print(count)