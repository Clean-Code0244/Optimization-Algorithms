import random

def Movement(array):
    randomly_selected_index = random.randint(0,len(array)-1)
    randomly_generated_number = random.randint(-2,2)
    array[randomly_selected_index] += randomly_generated_number
    if(array[randomly_selected_index] > 100):
        array[randomly_selected_index] = 100
    if(array[randomly_selected_index] < -100):
        array[randomly_selected_index] = -100
    return array

def fitness_function(array):
    total = 0
    for i in range(len(array)):
        total += array[i]**2
    return total






def Hill_Climbing():
    my_array = [random.randint(-100,100) for i in range(10)]
    #for i in range(10):
    #   my_array.append(random.randint(-100, 100))
    old_fitness = fitness_function(my_array)
    print("Old Fitness : ",old_fitness)
    print("----------------------------------------------------------------")
    
    max_Iterations = 10000
    number = 0
    while number <  max_Iterations:
        new_array = my_array.copy()
        if fitness_function(my_array)>fitness_function(Movement(new_array)):
            print("Iteration Number : ",number+1,"\tOld fitness : ",fitness_function(my_array),"\tNew Fitness : ",fitness_function(Movement(new_array)))
            my_array = new_array
            
        number += 1
    print("---------------------------------------------------------------")    
    new_fitness = fitness_function(my_array)
    print("Old Fitness : ",new_fitness)
    print(my_array)
        
        

Hill_Climbing()
    
