import re, math

with open('2023/day2/data.txt', 'r')as games:
    games = games.read().split("\n")

sum= 0

for i in games:
    max = {"red": 0, "green": 0, "blue": 0}
    gameNum, game = i.split(":")
    draws = game.split(";")#each individual draw
    
    print(f"\n\n{gameNum}")
    
    for j in draws: 
        inp = {"red": 0, "green": 0, "blue": 0}
        
        #populates inp and checks it against max  
        for color in max:
            inp[color] = int(re.search(rf"(\d+) {color}",j).group(1)) if re.search(rf"(\d+) {color}",j) else 0
            print(inp)
            if max[color] < inp[color]:
                print(f"{color}: max({max[color]}) < draw({inp[color]})", end = "\n\n")
                max[color] = inp[color]
            else:
                print(f"{color}: max({max[color]}) > draw({inp[color]})", end = "\n\n")
         
    power = math.prod(max.values())
    sum += power 
                       
print(f"Sum = {sum}")
    