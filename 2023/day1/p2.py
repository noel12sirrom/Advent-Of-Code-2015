with open('2023/day1/data.txt', 'r') as data:
    data = data.read().split("\n")

numberList = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
total = 0
count = 0 #used to debug and keep track of what line is currently being read

for i in data:
    count +=1
    numbers=[]
    strNum = ''
    
    for j in i:
        
        if j.isdigit():
            numbers.append(j) 
        else: #if character is not a digit it adds the character to a string until it spells out a digit
            strNum += j 
            
        for k in numberList:
            if  k in strNum:
                numbers.append(numberList[k])
                '''reassign strNum once it spells out a digit, the reason its not strNum = '' 
                is for cases like 'twone' where it would only  '''
                strNum = strNum[-1] 
    
    print(f"({count}). {numbers} |  {numbers[0]}{numbers[-1]}")     
    #add strings together then turn into an int to add to total
    total += (int(numbers[0] + numbers[-1]))    

    
print(total)
        