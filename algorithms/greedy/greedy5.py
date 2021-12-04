knightPosition = "c1"

positions = []
possiblePositionCOunt =0


def main():
    for i in range(8):
        row = []
    for j in range(8):
        row.append(0)
    positions.append(row)
    print(positions)

    xNo = getXNumber(knightPosition[0])
    yNo = getYNumber(knightPosition[1])
    print(xNo, yNo)
    count =0
    # check
    directionX = [2,2,-2,-2,1,-1,1,-1]
    directionY = [1,-1,1,-1,2,2,-2,-2]
    for i in range(len(directionX)):
        destinationX = xNo + directionX[i]
        destinationY = yNo + directionY[i]
        if destinationX >=1 and destinationX <=8 and destinationY >=1 and destinationY <=8 :
            count+=1
    print(count)
        # destinoation
def getXNumber(column):
    return ord(column) - ord("a") +1
    
def getYNumber(row):
    return int(row)


main()