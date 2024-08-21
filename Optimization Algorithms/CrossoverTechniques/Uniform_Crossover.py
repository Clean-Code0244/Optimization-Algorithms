import random

def uniform_crossover(parent1, parent2, probability):
    child1 = []
    child2 = []
    for i in range(len(parent1)):
       
        if random.random() < probability:
            
            child1.append(parent1[i])
            child2.append(parent2[i])
            
        else:
            
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1,child2


parent1 = [1, 2, 3, 4, 5]
parent2 = [6, 7, 8, 9, 10]
probability = 0.5  

print("Parent 1:", parent1)
print("Parent 2:", parent2)

child1,child2 = uniform_crossover(parent1, parent2, probability)
print("Child1:", child1)
print("Child2:", child2)
