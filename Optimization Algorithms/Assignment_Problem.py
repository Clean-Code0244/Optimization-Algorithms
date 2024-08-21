import random


def calculate_cost(arr1,arr2):
    cost = 0
    for i in range(len(arr1)):
        cost += arr1[i][arr2[i]]
        
    return cost

def change_the_list(arr):
    r1 = random.randint(0,len(arr)-1)
    r2 = random.randint(0,len(arr)-1)
    
    arr[r1],arr[r2] = arr[r2],arr[r1]
        
            
def main():
    job_worker_costs = [
        [25, 15, 20, 11, 7],
        [32, 30, 35, 22, 9],
        [5, 45, 50, 32, 11],
        [41, 21, 30, 12, 45],
        [21, 22, 4, 3, 12]
    ]
    
    iteration = 10000
    cost1 = float("inf")
    random_array = []
    
    for i in range(len(job_worker_costs)):
        random_array.append(i)
        
    best_match = []
    while iteration > 0:
        
        retval = calculate_cost(job_worker_costs,random_array)
        
        if retval < cost1:
            cost1 = retval
            best_match =  random_array.copy()
        random.shuffle(random_array)
        iteration -= 1
    
    for i in range(len(best_match)):
        print(str(i+1)+". job is assigned to : "+str(best_match[i]+1)+". worker",end="")
        print()
        
    print("Min Cost : ", cost1)

main()
