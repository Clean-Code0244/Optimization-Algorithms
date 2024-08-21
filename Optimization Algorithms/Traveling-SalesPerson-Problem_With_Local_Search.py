import random

#YANLIŞ HESAPLAMA YAPIYOR
def calculate_distance(graph):
    distance = 0
    my_node = -1
    for i in range(len(graph[0])):
        if graph[0][i] == 0:
            my_node = i
    for i in range(1,len(graph)):
        distance += graph[i][my_node]
        if i == len(graph) - 1:
            distance += graph[i][my_node]
            #Geri dönüş yolu
        
    return distance

def genreate_another_graph(graph):
    randomly_selected_index1 = random.randint(0,len(graph)-1)
    randomly_selected_index2 = random.randint(0,len(graph)-1)
    graph[randomly_selected_index1],graph[randomly_selected_index2] = graph[randomly_selected_index2],graph[randomly_selected_index1]
    
def copy_full_array(arr1):
    
    arr2 = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr2.append(arr1[i][j])
    return arr2

    
def main():
    graph = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]
    best_rotation = []
    min_distance = calculate_distance(graph)
    
    for a in graph:
        print(a)
    print(calculate_distance(graph))
    print("----------------------------------")
    
    for i in range(100):
        

        genreate_another_graph(graph)
        for b in graph:
            print(b)
        c = calculate_distance(graph)
        print(c)
        print("----------------------------------")
        if c < min_distance:
            min_distance = c
            best_rotation = graph
        
    print("Best Rotation : ")
    for x in best_rotation:
        print(x)
    print("Minimum Distance : ", min_distance)
    
        


main()