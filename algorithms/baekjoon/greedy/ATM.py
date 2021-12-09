#
length = int(input())
p = [int(x) for x in input().split(" ",length)]

p = sorted(p)

minSum =0
for i in range(length):
    minSum += p[i] * (length-i)
print(minSum)