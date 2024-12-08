data = open("day3/data.txt", "r").read().splitlines()

coords = [
    (-1, -1),# Top-left
    (-1, 0), # Up
    (-1, 1), # Top-right
    
    (0, -1), # Left
    (0, 1),  # Right
    
    (1, -1), # Bottom-left 
    (1, 0),  # Down
    (1, 1)   # Bottom-right 
]

coordsWithNumbers = []
grid = []
partsNumbers = []

def checkForDigits(r, c):
    for x,y in coords:
        #print(f"checking coords {x},{y}", end=" | ")
        rr,cc =  r+x, c+y
        #print(grid[rr][cc])
        
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]):
            if (rr,cc) not in coordsWithNumbers:
                if grid[rr][cc].isdigit():
                    #print("catch: ",grid[rr][cc])
                    getNumber(rr,cc) #if a digit is found it trys to collect the whole numbeer

def getNumber(r,c):
    number = ""
    
    
    def findStart():
        nonlocal c
        #replaced with chatgpt code
        while c > 0 and grid[r][c - 1].isdigit():  
            c -= 1
                
    findStart()  # Adjust c to the start of the number
    
    #gets number and saves coordinateres with numebr so that th number doesnt come up twice           
    while c < len(grid[r]) and grid[r][c].isdigit():
        number+=grid[r][c]
        coordsWithNumbers.append((r,c))
        c+=1
        
    partsNumbers.append(int(number))

#creates a 2d grid with DATA.TXTA 
for row in data:
    grid.append(list(i for i in row))   


symbols = "!@#$%&*-+=/"

for r, row in enumerate(data):
    #coordsWithNumbers = []
    for c, char in enumerate(row):
        
        if char in symbols:
            #print(f"found {char} in row {r}")
            checkForDigits(r, c) #checks for didgits adjecent or perpendicular to this point

print(sum(partsNumbers))
            