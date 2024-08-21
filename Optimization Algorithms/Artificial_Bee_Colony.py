import random
import math

def initial_solution(pop_size,dim,lover_bound,upper_bound):
    return [[random.uniform(lover_bound,upper_bound) for _ in range(dim)] for _ in range(pop_size)]
    
def fitness_function(solution):
    sum = (solution[0]-10)**2 + (solution[1]-5)**2 + (solution[2]-8)**2
    return math.sqrt(sum)

def movement(solution,lower_bound,upper_bound):
    phi = random.uniform(-1,1)
    new_solution = []
    for x in solution:
        delta = phi * (random.random() - 0.5)  # Çözümü biraz kaydırmak için delta
        new_x = x + delta
        # Sınırları aşmamak için kontrol
        new_x = min(max(new_x, lower_bound), upper_bound)
        new_solution.append(new_x)
    return new_solution
        
        
    
def abc(pop_size, dim, lower_bound, upper_bound, max_iter, limit):
    population = initial_solution(pop_size, dim, lower_bound, upper_bound)
    objective_values = [fitness_function(x) for x in population]
    
    trial_counter = [0]*pop_size
    
    
    best_solution = min(population, key=lambda sol: fitness_function(sol))
    best_value = fitness_function(best_solution)
    
    for iteration in range(max_iter):
        #Employee bees
        for i in range(pop_size):
            k = random.randint(0,pop_size-1)
            while k == i:
                k = random.randint(0,pop_size-1)
                
            new_solution = movement(population[i],lower_bound,upper_bound)
            new_objective = fitness_function(new_solution)
            
            if new_objective < objective_values[i]:
                population[i] = new_solution
                objective_values[i] = new_objective
                trial_counter[i] = 0
            else:
                trial_counter[i] += 1
        
        #Onlooker bees
        total_fitness = sum(1.0 / (1.0 + value) for value in objective_values)
        fitness = [1.0 / (1.0 + value) / total_fitness for value in objective_values]
        
        for i in range(pop_size):
            if random.random() < fitness[i]:
                
                k = random.randint(0,pop_size-1)
            while k == i:
                k = random.randint(0,pop_size-1)
                
            new_solution = movement(population[i],lower_bound,upper_bound)
            new_objective = fitness_function(new_solution)
            
            if new_objective < objective_values[i]:
                population[i] = new_solution
                objective_values[i] = new_objective
                trial_counter[i] = 0
            else:
                trial_counter[i] += 1
                
        #Scout bees
        for i in range(pop_size):
            if trial_counter[i] >= limit:
                # Çözüm çok uzun süre iyileşmediyse, yeni rastgele bir çözüm üret
                population[i] = [random.uniform(lower_bound, upper_bound) for _ in range(dim)]
                objective_values[i] = fitness_function(population[i])
                trial_counter[i] = 0  # Sıfırla

        # En iyi çözümü kontrol et
        current_best_solution = min(population, key=lambda sol: fitness_function(sol))
        current_best_value = fitness_function(current_best_solution)

        if current_best_value < best_value:
            best_solution = current_best_solution
            best_value = current_best_value

        print(f"Iteration {iteration + 1}: Best Value = {best_value}")

    return best_solution, best_value
                

 # ABC algoritmasını çalıştırmak için parametreler
pop_size = 20  # Popülasyon boyutu
dim = 3       # Çözüm uzayının boyutu
lower_bound = -10  # Çözüm uzayının alt sınırı
upper_bound = 10   # Çözüm uzayının üst sınırı
max_iter = 1000  # Maksimum yineleme sayısı
limit = 20      # Keşif arıları için limit

best_solution, best_value = abc(pop_size, dim, lower_bound, upper_bound, max_iter, limit)

print(f"Best Solution: {best_solution}")
print(f"Best Value: {best_value}")           
        