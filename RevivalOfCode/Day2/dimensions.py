
with open('python_sandbox/RevivalOfCode/Day2/boxdimesions.txt', 'r') as dimensions:
    dimensions = dimensions.read().split("\n")
  
def Question1():
        def wrapping_paper(l, w, h):
                lw = l * w
                wh = w * h
                hl = h * l

                slack = min([lw, wh, hl])

                answer = 2 * lw + 2 * wh + 2 * hl + slack

                return answer

        _answer = 0
 
        for dimension in dimensions:
            a, b, c = dimension.split("x")
            a, b, c = int(a), int(b), int(c)
                
            _answer += (wrapping_paper(a, b, c))

        print(f"The elves need {_answer}feet of wrapping paper.")
Question1()    
    
    
def Question2 ():
            def question2(l, w, h):
                    total_lenght_needed = 0
                    
                    ribbon_lenght = 0
                        
                    lw = l + w
                    wh = w + h
                    hl = h + l
                    bow = l * h* w
                    
                    ribbon= min([lw, wh, hl])
                    ribbon_lenght += (ribbon)*2
                    total_lenght_needed += bow + ribbon_lenght
                    
                    return total_lenght_needed
                
            ribbon_lenght_needed= 0
            for dimension in dimensions:
                a, b, c = dimension.split("x")
                a, b, c = int(a), int(b), int(c)
                
                ribbon_lenght_needed += (question2(a, b, c))    
            
            print(f"The elves need {ribbon_lenght_needed}feet of ribbon material.")
Question2()
   