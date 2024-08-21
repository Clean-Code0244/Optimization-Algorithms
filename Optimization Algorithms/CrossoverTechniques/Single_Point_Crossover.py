import random

def single_point_crossover(parent1, parent2):
    
    crossover_point = random.randint(1, len(parent1) - 1)  # 1'den son gen hariç herhangi bir noktada keser

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

# Örnek kullanım
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parent2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

child1, child2 = single_point_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
