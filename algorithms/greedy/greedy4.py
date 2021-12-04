# 상하좌우
import datetime

N = 3
# start = 0
# end = 3*10000 + 5959


start = datetime.datetime(1, 1, 1, 0,0,0)
end = datetime.datetime(1, 1, 1, N,0,0)

currentTime = start
count = 0
while True:
    if currentTime == end:
        break
    else:
        currentTime += datetime.timedelta(seconds=1)
        # print(currentTime)
        if currentTime.hour == 3 or currentTime.minute == 3 or currentTime.second ==3:
            count +=1

print(count)