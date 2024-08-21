import random
import math

def Movement(graph):

    numOfCities = len(graph) 
    cities, newPath = [] ,[]

    for i in range(1, numOfCities+1):
        cities.append(i) 
    
    for i in range(numOfCities):
        city = random.choice(cities)
        newPath.append(city)
        cities.remove(city)

    return newPath 



def Evaluate(graph, newPath):

    distance = 0

    for i in range(len(newPath)-1):
        distance += graph[newPath[i]-1][newPath[i+1]-1]
    
    distance += graph[newPath[-1]-1][newPath[0]-1]


    return distance




def main():
    
    graph = [[0,2,4,3,5],
             [2,0,7,6,2],
             [4,7,0,3,4],
             [3,6,3,0,8],
             [5,2,4,8,0]]
    

    iteration, MaxIt = 0, 100
    bestDistance = float("inf")
    
    temperature = 100
    temperatureCoefficient = 0.99

    while iteration < MaxIt:

        path = Movement(graph)
        distance = Evaluate(graph, path)

        if distance < bestDistance: 
            bestDistance = distance
            bestPath = path.copy()
            print(f"{iteration+1}. try -> Best path so far: {bestPath} with {bestDistance} distance")
        

        else:  
            
            
            
            delta = distance - bestDistance
            if random.random() < math.exp(-delta/temperature):
                bestDistance = distance
                bestPath = path.copy()
                print(f"{iteration+1}. try -> Best path so far: {bestPath} with {bestDistance} distance")
        
        temperature *= temperatureCoefficient

        iteration += 1

    print(f"\n\nBest path: {bestPath}\nBest Distance: {bestDistance}")


main()