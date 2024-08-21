import numpy as np
import matplotlib.pyplot as plt
class AntColony:
    def __init__(self, distance_matrix, num_ants, num_iterations, alpha=1, beta=2, rho=0.5, q=100, initial_pheromone=1):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        self.initial_pheromone = initial_pheromone
        self.pheromone_matrix = np.ones((self.num_cities, self.num_cities)) * initial_pheromone
        np.fill_diagonal(self.pheromone_matrix, 0)
    def run(self):
        best_distance = float('inf')
        best_route = []
        for iteration in range(self.num_iterations):
            all_routes = []
            all_distances = []
            for ant in range(self.num_ants):
                route = self._build_route()
                distance = self._calculate_distance(route)
                all_routes.append(route)
                all_distances.append(distance)
                if distance < best_distance:
                    best_distance = distance
                    best_route = route
            self._update_pheromones(all_routes, all_distances)
        return best_route, best_distance
    def _build_route(self):
        route = []
        visited = set()
        current_city = np.random.randint(0, self.num_cities)
        route.append(current_city)
        visited.add(current_city)
        while len(visited) < self.num_cities:
            next_city = self._select_next_city(current_city, visited)
            route.append(next_city)
            visited.add(next_city)
            current_city = next_city
        route.append(route[0])  # Return to the starting city
        return route
    def _select_next_city(self, current_city, visited):
        probabilities = self._calculate_probabilities(current_city, visited)
        return np.random.choice(range(self.num_cities), p=probabilities)
    def _calculate_probabilities(self, current_city, visited):
        pheromones = np.copy(self.pheromone_matrix[current_city])
        pheromones[list(visited)] = 0
        visibility = 1 / (self.distance_matrix[current_city] + 1e-10)
        probabilities = np.power(pheromones, self.alpha) * np.power(visibility, self.beta)
        probabilities /= np.sum(probabilities)
        return probabilities
    def _calculate_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i], route[i + 1]]
        return distance
    def _update_pheromones(self, all_routes, all_distances):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    self.pheromone_matrix[i, j] *= (1 - self.rho)
                    self.pheromone_matrix[i, j] += self.q / np.mean(all_distances)
def plot_tsp_route(distance_matrix, route):
    num_cities = len(route)
    city_positions = np.zeros((num_cities, 2))
    for i in range(num_cities):
        city_positions[i] = [i, route[i]]
    plt.figure(figsize=(8, 6))
    plt.scatter(city_positions[:, 0], city_positions[:, 1], c='b', marker='o', s=100)
    plt.plot(city_positions[:, 0], city_positions[:, 1], 'k--')
    for i in range(num_cities):
        plt.text(city_positions[i, 0], city_positions[i, 1], str(i), fontsize=12, ha='center', va='center')
    plt.title("TSP En İyi Rota")
    plt.xlabel("Şehirler")
    plt.ylabel("Sıralama")
    plt.xticks(range(num_cities))
    plt.yticks(range(num_cities))
    plt.grid(True)
    plt.show()
def main():
    # Example usage
    distance_matrix = np.array([
        [0, 5, 8, 3, 7, 1],
        [5, 0, 2, 10, 8, 4],
        [8, 2, 0, 3, 10, 5],
        [3, 10, 3, 0, 2, 7],
        [7, 8, 10, 2, 0, 6],
        [1, 4, 5, 7, 6, 0],
    ])
    num_ants = 10
    num_iterations = 100
    alpha = 1
    beta = 2
    rho = 0.5
    q = 100
    initial_pheromone = 1
    ant_colony = AntColony(distance_matrix, num_ants, num_iterations, alpha, beta, rho, q, initial_pheromone)
    best_route, best_distance = ant_colony.run()
    print("Best route:", best_route)
    print("Best distance:", best_distance)
    plot_tsp_route(distance_matrix, best_route)
if __name__ == "__main__":
    main()