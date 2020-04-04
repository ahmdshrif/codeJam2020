
##Read Input 
num_of_cases = int(input()) 

# def get_colom (Matix , i ):

row [] = [0 for i in range(num_of_cases)]
colom [] = [0 for i in range(num_of_cases)]
Sum[] = [0 for i in range(num_of_cases)]

for case in range(num_of_cases) :
    size_the_matrix = int(input())
    Matix = [ None for i in range(size_the_matrix)]
    for i in range(size_the_matrix):
        Matix[i] = list(map(int, input().strip().split()))

    #num of reapetd row : 
    for i in range(size_the_matrix):
        if len(set(Matix[i])) < len(Matix[i]):
            row[case] += 1
    # print(row)

    #sum of diagonas 
    for i in range(size_the_matrix):
        Sum[case] += Matix[i][i]
    # print(Matix)

    Matix = list(zip(*Matix))
    
    #num of reapetd colom : 
    for i in range(size_the_matrix):
        if len(set(Matix[i])) < len(Matix[i]):
            colom[case] += 1
    # print(clom)
for case in range(num_of_cases):
    print("Case #{}: {} {} {}".format(case+1, Sum[case] , row[case] , colom[case] ), flush = True)

    

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

