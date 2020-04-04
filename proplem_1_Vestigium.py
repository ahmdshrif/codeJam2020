
##Read Input 
num_of_cases = int(input()) 

for case in range(num_of_cases) :
    size_the_matrix = int(input())
    Matix = [ None for i in range(size_the_matrix)]
    for i in range(size_the_matrix):
        Matix[i] = list(map(int, input().strip().split()))
    
    

# test 


# input : - 
 
# 1
# 4
# 1 2 3 4
# 2 1 4 3
# 3 4 1 2
# 4 3 2 1
# 4
# 2 2 2 2
# 2 3 2 3
# 2 2 2 3
# 2 2 2 2
# 3
# 2 1 3
# 1 3 2
# 1 2 3
# output : - 


# Case #1: 4 0 0
# Case #2: 9 4 4
# Case #3: 8 0 2

