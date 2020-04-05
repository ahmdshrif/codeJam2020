#read inputs 
num_of_cases = int(input()) 

def is_time_overlab (calender , time2):
    St2 = time2[0]
    Et2 = time2[1]
    for i in range(St2,Et2):
        if i in calender : 
            return True
    
    return False

def add_to_clender(calender , time2):
    St2 = time2[0]
    Et2 = time2[1]
    for i in range(St2,Et2):
        calender.add(i)
    

for case in range(num_of_cases) : 
    num_of_activities  =  int(input())
    activities  = [[]for i in range(num_of_activities)]
    
    for i in range(num_of_activities) :
        activities[i] = list(map(int, (input()+" " + str(i)).strip().split()))

    activities.sort()
    # print(activities)

    result = ["" for i in range(num_of_activities)]
    J_calender = set()
    C_calender = set()
    IMPOSSIBLE = False
    for i in range(num_of_activities):
        if not(is_time_overlab(J_calender , activities[i])):
            result[activities[i][2]] = "J"
            add_to_clender(J_calender , activities[i])

        elif not(is_time_overlab(C_calender , activities[i])):
            add_to_clender(C_calender , activities[i])
            result[activities[i][2]] = "C"

        else : 
            IMPOSSIBLE = True
            # result = "IMPOSSIBLE"
            break
 

    if IMPOSSIBLE :
        print("Case #{}: {}".format(case+1, "IMPOSSIBLE" ), flush = True)

    else:
        print("Case #{}: {}".format(case+1, "".join(result) ), flush = True)