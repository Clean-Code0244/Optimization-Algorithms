import random

def cut_and_slice_crossover(parent1, parent2):
    length = len(parent1)
    cut_point = random.randint(1, length - 1)  

    
    child1 = parent1[:cut_point] + parent2[cut_point:]

    
    child2 = parent2[:cut_point] + parent1[cut_point:]

    return child1, child2


parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parent2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

child1, child2 = cut_and_slice_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
