import random

def create_random_solution(values):
    solution = []
    for i in range(len(values)):
        solution.append(random.randint(0,1))
    return solution

def is_that_solution_valid(weights,solution,capacity):
    total_weight = 0
    
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            
    if total_weight > capacity:
        return False
    return True
    
def calculate_value(weights,values,capacity,solution):
    total_value = 0
    for i in range(len(values)):
        if is_that_solution_valid(weights,solution,capacity):
            total_value += values[i]*solution[i]
    return total_value

def calculate__best_solution(weights,values,capacity):
    max = 0
    number = 1000
    while number > 0:
        is_that_best = calculate_value(weights,values,capacity,create_random_solution(weights))
        if is_that_best > max:
            max = is_that_best
        number = number - 1
    return max

  

values = [60,100,120]
weights = [10,20,30]
capacity = 50

best_solution = calculate__best_solution(weights.copy(),values.copy(),capacity)
print("The best Solution is : ",best_solution)