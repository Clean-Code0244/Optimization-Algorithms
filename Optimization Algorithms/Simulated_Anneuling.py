import random
import math

def initial_Array():
    
    my_array = []
    for i in range(10):
        my_array_2 = []
        for j in range(10):
            my_array_2.append(random.randint(0,100))
        my_array.append(my_array_2)
    return my_array

def fitness_function(array):
    
    total = 0
    for i in array:
        for j in i:
            total += j**2
    return total

def copy_full_array(array):
    my_array = []
    for i in range(len(array)):
        second_array = []
        for j in range(len(array[i])):
            second_array.append(array[i][j])
        my_array.append(second_array)
    return my_array
def Movement(array):
    
    my_array = copy_full_array(array)
    randomly_selected_index1 = random.randint(0,len(array)-1)
    randomly_selected_index2 = random.randint(0,len(array[0])-1)
    randomly_generated_number = random.randint(0,10)
    my_array[randomly_selected_index1][randomly_selected_index2] = randomly_generated_number
    #print(randomly_selected_index1,randomly_selected_index2,randomly_generated_number)
    return my_array

def is_that_acceptable_solution(initial_cost, new_cost,temprature):
    
    if new_cost<initial_cost:
        return 1
    return math.exp((initial_cost - new_cost) / temprature)

def show_arrays(arr1,arr2):
    
    for i in range(len(arr1)):
        print(arr1[i],"\t\t",arr2[i])
        


def simulated_annealing():
    
    temprature = 100
    cooling_rate = 0.9
    max_iteration = 10000
    array1 = initial_Array()
    num = fitness_function(array1)
    d = copy_full_array(array1)
    initial_cost = fitness_function(array1)
    for i in range(0,max_iteration):
        array2 = Movement(array1)
        #show_arrays(array1,array2)
        new_cost = fitness_function(array2)
        
        if is_that_acceptable_solution(initial_cost, new_cost,temprature) > random.random():
            array1 = array2
            initial_cost = new_cost
        temprature *= cooling_rate
        
    return array1,initial_cost,d,num
    
a,b,d,num = simulated_annealing()
 
for e in d:
    print(e)
print("-----------------------------------")
print(num)
for c in a:
    print(c)
print("-----------------------------------")
print(b)