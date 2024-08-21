import random

def singlePointCrossover(parent1, parent2):

    point = random.randint(1, len(parent1)-1)
    child = parent1[:point] + parent2[point+1:]

    return child



def Fitness(knapsack, weights, values):

    weight, value = 0, 0
    for i in range(len(knapsack)):
        if (knapsack[i] == 1):
            weight += weights[i]
            value += values[i]

    return weight, value




def main():
    capacity = 40
    weights = [7, 5, 10, 15, 5, 3, 8, 4, 9, 12]
    values = [10, 15, 5, 8, 20, 10, 7, 17, 5, 3]

    iteration, maxIteration = 0, 100
    bestValue, bestWeight, bestKnapsack = 0, 0, None

    parent1, parent2 = [], []
    for i in range(len(values)):
        parent1.append(random.choice([0, 1]))
        parent2.append(random.choice([0, 1]))

    while iteration < maxIteration:

        knapsack = singlePointCrossover(parent1, parent2)
        currentWeight, currentValue = Fitness(knapsack, weights, values)

        if (currentWeight < capacity and currentValue > bestValue):
            bestValue = currentValue
            bestWeight = currentWeight
            bestKnapsack = knapsack.copy()
            print(f"\n{iteration+1}. try, Best Knapsack so far: {bestKnapsack}\nBest Value so far: {bestValue} with {bestWeight} weights")
    
        iteration += 1
    
    print(f"\nBest Knapsack: {bestKnapsack}\nBest Value: {bestValue}\nWeight: {bestWeight}")

main()