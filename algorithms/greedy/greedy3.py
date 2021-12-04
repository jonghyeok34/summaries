# max  group count

# 공포도 X

infoList = [7,3,1,2,3,4,5,6]

infoList = sorted(infoList)

totalGroup = []
group = []
groupCount = 0
for x in infoList:
    groupMembers = len(group) +1
    
    if groupMembers >= x:
        print(x)
        totalGroup.append(group.copy())
        groupCount+=1
        group = []
    else:
        group.append(x)
print(totalGroup)
print(groupCount)