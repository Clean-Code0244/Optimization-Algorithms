import random

def generate_adjaceny_list(parent):
    adjacency_dictionary = {}
    
    for i in range(len(parent)):
        adjacency_dictionary[parent[i]] = []
        adjacency_dictionary[parent[i]].append(parent[(i+1) % len(parent)])
        adjacency_dictionary[parent[i]].append(parent[(i-1) % len(parent)])
    return adjacency_dictionary

def Edge_Recombination(parent1,parent2):
    
    all_genes = list(set(parent1+parent2))
    child = []
    
    adjacency_list_parent1 = generate_adjaceny_list(parent1)
    adjacency_list_parent2 = generate_adjaceny_list(parent2)
    
    random_number = random.randint(0, len(all_genes)-1)
    current_gene = all_genes[random_number]
    
    child.append(current_gene)
    all_genes.remove(current_gene)
    
    while all_genes:
        #Burda dictionaryden gelen liste elemanlarını birleştiriyorum.
        neighbors = adjacency_list_parent1[current_gene] + adjacency_list_parent2[current_gene]
        
        # Komşu genlerin sayılarını bul
        neighbor_counts = {gene : neighbors.count(gene) for gene in neighbors}
        
        # Komşu genlerden en az komşusu olanı seç
        min_count = min(neighbor_counts.values())
        
        #En az komşuya sahip olan node ları listele
        neighbors_with_min_count = [gene for gene, count in neighbor_counts.items() if count == min_count]
        
        #Eğer 1 den fazla elamn varsa neighbors_with_min_count listesinde
        if len(neighbors_with_min_count)> 1:
            random_number = random.randint(0,len(neighbors_with_min_count)-1)      
            next_gene =   neighbors_with_min_count[random_number]
        else:
            next_gene = neighbors_with_min_count[0]
            
        child.append(next_gene)
        
        all_genes.remove(next_gene)
        
        #Komşuluk listelerinden ilgili gen silinir
        for gene , neighbors in adjacency_list_parent1.items():
            if  next_gene in neighbors:
                neighbors.remove(next_gene)
    
        for gene , neighbors in adjacency_list_parent2.items():
            if  next_gene in neighbors:
                neighbors.remove(next_gene)
        
        current_gene = next_gene
    
    return child

parent1 = [1, 2, 3, 4, 5]
parent2 = [3, 5, 2, 1, 4]

print("Parent 1:", parent1)
print("Parent 2:", parent2)

child = Edge_Recombination(parent1, parent2)
print("Child:", child)
    
    