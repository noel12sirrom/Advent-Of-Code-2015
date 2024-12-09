import re
cards= open("2023/day4/data.txt", "r").read().splitlines() 
total = 0
for card in cards:
    matches = 0  
    winningNums = []
    myNums = []
    card = re.sub(r"Card\s*(\d+): ",  "", card)
    print(card)
    winning_str, my_str = card.split("|")
    
    winningNums = list(map(int, winning_str.split()))
    myNums = list(map(int, my_str.split()))
    
    for num in winningNums:
        if num in myNums and matches != 0:
            matches = matches* 2
        elif num in myNums and matches == 0:
            matches +=1
    
    #print("found {matches} matches")
    total += matches
    

print(total)