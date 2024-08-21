import random

# Başlangıç çözümünü oluşturmak için rastgele bir çözüm üreten fonksiyon
def generate_initial_solution(num_cities):
    return random.sample(range(1, num_cities + 1), num_cities)


# Verilen bir çözümün toplam mesafesini hesaplayan fonksiyon
def calculate_total_distance(solution, distances):
    total_distance = 0
    num_cities = len(solution)
    for i in range(num_cities - 1):
        city1 = solution[i]
        city2 = solution[i + 1]
        total_distance += distances[city1 - 1][city2 - 1]
    total_distance += distances[solution[-1] - 1][solution[0] - 1]
    
    return total_distance

# Verilen bir çözümün komşu çözümlerini üreten fonksiyon
def generate_neighbors(solution):
    neighbors = []
    num_cities = len(solution)
    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap i and j
            neighbors.append(neighbor)
    #print(neighbors)
    return neighbors

# Tabu Search algoritması
def tabu_search(initial_solution, distances, max_iterations, tabu_size):
    current_solution = initial_solution[:]
    best_solution = initial_solution[:]
    tabu_list = []
    num_cities = len(initial_solution)
    
    for i in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        #Her seferinde komşu oluşturmak yerine eldeki komşularla arama yapıyoruz
        best_neighbor = None
        best_distance = float('inf')
        
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                
                distance = calculate_total_distance(neighbor, distances)
                if distance < best_distance:
                    best_neighbor = neighbor
                    best_distance = distance
        
        if best_neighbor is None:
            break
        
        current_solution = best_neighbor
        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        if best_distance < calculate_total_distance(best_solution, distances):
            best_solution = best_neighbor
    
    return best_solution, calculate_total_distance(best_solution, distances)

# Örnek kullanım
if __name__ == "__main__":
    # Mesafeler matrisi (örneğin, şehirler arasındaki mesafeler)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    num_cities = len(distances)
    initial_solution = generate_initial_solution(num_cities)
    #print(initial_solution)
    
    # Tabu Search parametreleri
    max_iterations = 1000
    tabu_size = 10
    
    # Tabu Search uygulaması
    best_solution, best_distance = tabu_search(initial_solution, distances, max_iterations, tabu_size)
    
    print("En iyi çözüm:", best_solution)
    print("En iyi mesafe:", best_distance)
