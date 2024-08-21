import random

def generate_adjacency_list(parent1, parent2):
    adjacency_dictionary = {}
    
    for i in range(len(parent1)):
        # İki parent listesinden değişik genlerin komşuluklarını birleştir
        neighbors = set()
        neighbors.add(parent1[(i+1) % len(parent1)])
        neighbors.add(parent1[(i-1) % len(parent1)])
        
        adjacency_dictionary[parent1[i]] = neighbors
        
    for i in range(len(parent2)):
        adjacency_dictionary[parent2[i]].add(parent2[(i+1) % len(parent2)])
        adjacency_dictionary[parent2[i]].add(parent2[(i-1) % len(parent2)])
    
    return adjacency_dictionary

def Edge_Recombination(parent1, parent2):
    all_genes = parent1 + parent2  # Tüm genleri bir liste olarak oluştur
    child = []
    
    adjacency_list = generate_adjacency_list(parent1, parent2)
    
    random_gene = random.choice(all_genes)  # Rastgele bir gen seç
    current_gene = random_gene
    
    child.append(current_gene)
    
    num = all_genes.count(current_gene)
    for i in range(num):
        all_genes.remove(current_gene)
   
    while all_genes:
        neighbors = adjacency_list[current_gene]  # Komşuları al, eğer yoksa boş liste döndür
        
        if not neighbors:
            break  # Eğer komşu yoksa döngüyü sonlandır
        
        neighbor_counts = {}
        # Komşu genlerin sayılarını bul
        for gene in neighbors:
            neighbor_counts[gene] = len(adjacency_list[gene])
        
        # Komşu genlerden en az komşusu olanı seç
        min_count = min(neighbor_counts.values())
        
        # En az komşuya sahip olan genleri listele
        neighbors_with_min_count = [gene for gene, count in neighbor_counts.items() if count == min_count]
        
        if len(neighbors_with_min_count) > 1:
            next_gene = random.choice(neighbors_with_min_count)  # Rastgele birini seç
        else:
            next_gene = neighbors_with_min_count[0]
        
        child.append(next_gene)
        
        num = all_genes.count(next_gene)
        for i in range(num):
            all_genes.remove(next_gene)
            
        # Seçilen genin komşuluk listelerinden silinmesi
        for gene, neighbors in adjacency_list.items():
            if next_gene in neighbors:
                neighbors.remove(next_gene)
        
        current_gene = next_gene
    
    return child

parent1 = ['A', 'B', 'F', 'E', 'D', 'G', 'C']
parent2 = ['G', 'F', 'A', 'B', 'C', 'D', 'E']

print("Parent 1:", parent1)
print("Parent 2:", parent2)

child = Edge_Recombination(parent1, parent2)
print("Child:", child)
