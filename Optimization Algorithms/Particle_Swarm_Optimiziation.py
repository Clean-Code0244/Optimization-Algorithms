import random

def fitness(arr):
    result = 0
    for i in range(len(arr)-1):
        result += 100*(arr[i+1]-arr[i]**2)**2 + (arr[i]-1)**2
    return result

def initialize_population():
    return [[random.uniform(-5,5) for _ in range(5)] for _ in range(10)]

def global_best_array():
    return [random.uniform(-5,5) for _ in range(5)]

def velocity_array():
    return [[0]*5 for _ in range(10)]

def main():
    c1, c2 = 2, 2
    population = initialize_population()
    global_best = global_best_array()
    pbest = [row[:] for row in population]
    velocity = velocity_array()
    print("First global best",global_best)
    print("First populationbest",pbest)
    max_iteration = 100
    for _ in range(max_iteration):
        for y in range(len(population)):
            if fitness(population[y]) < fitness(pbest[y]):
                pbest[y] = population[y][:]
                if fitness(pbest[y]) < fitness(global_best):
                    global_best = pbest[y][:]
        print("Global best = ",fitness(global_best))
        for y in range(len(population)):
            for z in range(len(population[y])):
                velocity[y][z] = c1*random.random()*(pbest[y][z]-population[y][z]) + c2*random.random()*(global_best[z]-population[y][z])
                population[y][z] = population[y][z] + velocity[y][z]

    print("Last global best")
    print(global_best)
    print("Last population best ")
    print(pbest)

main()
