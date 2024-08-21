import random

def generate_random_solution(number):
    new_solution = []
    for i in range(number):
        new_solution.append(random.randint(0, 1))
    return new_solution

def single_point_crossover(arr1, arr2):
    rnd_number = random.randint(0, len(arr1) - 1)
    new_arr = arr1[:rnd_number] + arr2[rnd_number:]
    return new_arr

def fitness_function(arr1, arr2, arr3, capacity):
    sum_value = 0
    sum_weight = 0
    for i in range(len(arr3)):
        if arr3[i] == 1:
            sum_weight += arr1[i]
            sum_value += arr2[i]
    if sum_weight > capacity:
        sum_value = 0
    return sum_value, arr3

def main():
    value = [10, 15, 5, 8, 20, 10, 7, 17, 5, 3]
    weight = [7, 5, 10, 15, 5, 3, 8, 4, 9, 12]
    capacity = 3

    optimal_arr = [0] * len(value)
    max_value = 0
    for _ in range(10000):
        arr3 = generate_random_solution(len(value))
        arr4 = generate_random_solution(len(value))

        crossover_array = single_point_crossover(arr3, arr4)
        a, b = fitness_function(weight, value, crossover_array, capacity)
        if a > max_value:
            max_value = a
            optimal_arr = b

    print("Optimal solution:")
    for i in optimal_arr:
        print(i, end=" ")
    print("\nMax value:", max_value)

main()
