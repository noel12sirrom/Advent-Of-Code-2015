data = open("2024/day1/data.txt", "r").read().splitlines()
total = 0
left = []
right = []
minimums = []

for line in data:
    l,r = line.split()
    left.append(int(l))
    right.append(int(r))
    
while left:
    minimums= []
    minLeft = min(left)
    minRight =min(right)
    minimums.append(minLeft)
    minimums.append(minRight)
    left.remove(minLeft)
    right.remove(minRight)
    
    distance = max(minimums) - min(minimums)
    total += distance
        
print(total)

