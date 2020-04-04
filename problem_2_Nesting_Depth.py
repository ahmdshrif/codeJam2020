# read input 
num_of_cases = int(input()) 
String = ""
for case in range(num_of_cases):
    String =  str(input())

    result= ""
    num_of_open_parentheses = 0 
    for i in range(len(String)):
        curent_num = int(String[i])
        if  curent_num == 0 or num_of_open_parentheses == 0:
            result += ")" * num_of_open_parentheses
            result += "(" * curent_num 
            num_of_open_parentheses = curent_num
        
        elif num_of_open_parentheses > curent_num :
            result += ")" * (num_of_open_parentheses -curent_num) 
            num_of_open_parentheses -= (num_of_open_parentheses -curent_num)
        elif num_of_open_parentheses < curent_num :
            result += "(" * (curent_num- num_of_open_parentheses) 
            num_of_open_parentheses +=  (curent_num- num_of_open_parentheses) 
            
        result += String[i]
    result += ")" * num_of_open_parentheses

    print("Case #{}: {}".format(case+1, result ), flush = True)


"""
test cases
input
4
0000
101
111000
1

output
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)
"""