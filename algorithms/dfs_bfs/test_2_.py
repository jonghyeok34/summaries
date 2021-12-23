
n = 5
m = 6


maze = [
    "101010",
    "111111",
    "000001",
    "111111",
    "111111"
]
distanceCheck ={}

def setMinDistance(distance, prevX, prevY):
    
    print(distance,prevX, prevY)
    nextX = prevX
    if prevX+1<=n:
    
        nextX+=1
        if maze[nextX-1][prevY-1] != "0":
            newDistance = distance +1
            distanceCheck[f'{nextX}-{prevY}'] = newDistance
            setMinDistance(newDistance, nextX, prevY)
    nextY = prevY
    if prevY+1<=m:
        nextY+=1
        if maze[prevX-1][nextY-1] != "0":
            newDistance = distance +1
            distanceCheck[f'{prevX}-{nextY}'] = newDistance
            setMinDistance(newDistance, prevX, nextY)

setMinDistance(0 , 1,1)
print(distanceCheck[f'{n}-{m}'])    
    # return get