n = int(input())
foodStores = list(map(int, input().split()))
maxFood =[]

if len(foodStores) >1:
    maxFood.append(foodStores[0])
if len(foodStores)>2:
    maxFood.append(max(maxFood[0],foodStores[1]))
if len(foodStores)>3:
    for i in range(2, len(foodStores)):
        maxFood.append(max(maxFood[i-1], maxFood[i-2] + foodStores[i])
        )
        
# print(max(earnFoodData[0], earnFoodData[1] ))
print(maxFood)