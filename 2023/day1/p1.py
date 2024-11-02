with open('2023/day1/data.txt', 'r') as data:
    data = data.read().split("\n")

total = 0

for i in data:
    tempList=[]
    
    for j in i:
        if j.isdigit():
            tempList.append(j)    
    total += (int(tempList[0] + tempList[-1])) 
    
print(total)
        