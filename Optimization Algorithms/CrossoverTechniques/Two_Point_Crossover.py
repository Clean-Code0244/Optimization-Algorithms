import random

def two_point_crossover(parent1, parent2):
    length = len(parent1)
    crossover_points = sorted(random.sample(range(1, length), 2))
    print(crossover_points)
    child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
    child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]

    return child1, child2

# Örnek kullanım
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parent2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

child1, child2 = two_point_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
