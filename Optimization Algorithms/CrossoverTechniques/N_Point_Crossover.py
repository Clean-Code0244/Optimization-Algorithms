import random

def n_point_crossover(parent1, parent2, n):
    length = len(parent1)
    crossover_points = sorted(random.sample(range(1, length), n))
    print(crossover_points)

    child1 = []
    child2 = []
    last_point = 0

    for point in crossover_points:
        if (crossover_points.index(point) % 2) == 0:
            child1.extend(parent1[last_point:point])
            child2.extend(parent2[last_point:point])
        else:
            child1.extend(parent2[last_point:point])
            child2.extend(parent1[last_point:point])
        last_point = point

    child1.extend(parent1[last_point:])
    child2.extend(parent2[last_point:])

    return child1, child2

# Örnek kullanım
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parent2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 3  # İki noktada kesme

child1, child2 = n_point_crossover(parent1, parent2, n)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
