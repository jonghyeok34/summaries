N = int(input())


def getPacks(N):
    bigPacks = N // 5
    smallPacks = 0
    while True:
        left = N - bigPacks*5
        if left % 3 == 0:
            smallPacks = left//3
            break
        else:
            bigPacks -= 1
        if bigPacks == -1:
            return -1
    return bigPacks + smallPacks

    # if
    # print(bigPacks +smallPacks)


print(getPacks(N))
