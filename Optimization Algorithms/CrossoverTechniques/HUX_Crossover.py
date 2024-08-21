import random

def huxCrossover(parent1, parent2):

    child1 = parent1[:]
    child2 = parent2[:]
    hammingDistance = 0


    for i in range(len(parent1)):
        if (parent1[i] != parent2[i]):
            hammingDistance += 1
            randChoice = random.choice([0, 1])
            if randChoice == 1:
                child1[i] = parent2[i]
                child2[i] = parent1[i]
            else:
                continue

        else:
            continue


    return "Child1 ",child1, "Child2 ", child2, "Hamming distance ", hammingDistance


def main():
    parent1 = [1, 1, 0, 0, 0, 0, 1, 0]
    parent2 = [1, 0, 0, 1, 1, 0, 1, 1]

    print(huxCrossover(parent1, parent2))

main()