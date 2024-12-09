data = open("2024/day1/data.txt", "r").read().splitlines()
total = 0
left = []
right = []
minimums = []

for line in data:
    l,r = line.split()
    left.append(int(l))
    right.append(int(r))
    
for number in left:
    count = 0
    for num in right:
        if number == num:
            count += 1
    
    total += number * count

print(total)
        

