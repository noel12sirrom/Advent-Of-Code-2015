import re 

with open('2023/day2/data.txt', 'r')as games:
    games = games.read().split("\n")

    sum= 0
    
print("start--")
    
for i in games:

    i = re.sub(r"Game (\d+): ",  "", i)
    draws = i.split(";")#each individual draw
    
    #populates inp with  
    for j in draws: 
        inp = {"red": 0, "green": 0, "blue": 0}
        print(j, end=" | ")
        print()
            
        for color in max:
            inp[color] = int(re.search(rf"(\d+) {color}",j).group(1)) if re.search(rf"(\d+) {color}",j) else 0
            
            print(inp)
            print(color)
            if max[color] < inp[color]:
                print(f"max({max[color]}) < inp({inp[color]})", end = "\n\n")
                addGameNum = False
                break
            else:
                print(f"max({max[color]}) > inp({inp[color]})", end = "\n\n")
         
    if addGameNum:
        print(f"+{gameNum}")
        print()
        sumOfId += gameNum            
            
print(sumOfId)
    