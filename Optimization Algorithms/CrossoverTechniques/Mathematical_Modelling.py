from functools import reduce
import random
def create_initial_solution():
    return [random.randint(-5,5) for _ in range(5)]
def fitness(arr):
    return reduce(lambda acc, x: acc + x**2, arr, 0)

array = create_initial_solution()
print(fitness(array))
print(array)