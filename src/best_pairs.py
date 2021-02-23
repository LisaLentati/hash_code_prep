import numpy as np

def best_pairs(pizza_dict):

    num_pizza = len(pizza_dict.keys())
    pairs = {}
    
    for i in range(num_pizza):
        for j in range(i):
            len_pizza_1 = len(pizza_dict[i])
            len_pizza_2 = len(pizza_dict[j])
            distinct = len(set(pizza_dict[i] + pizza_dict[j]))
            pairs[(i,j)] = [len_pizza_1, len_pizza_2, distinct]
            
    
    return sorted(pairs.items(), key = lambda item: item[1][2])
        
