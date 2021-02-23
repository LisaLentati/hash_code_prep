

def twos(pizza_dict):

    num_pizza = len(pizza_dict.keys())
    pairs = {}
    
    for i in range(num_pizza):
        for j in range(i):
        
            len_pizza_1 = len(pizza_dict[i])
            len_pizza_2 = len(pizza_dict[j])
            distinct = len(set(pizza_dict[i] + pizza_dict[j]))
            pairs[(j,i)] = [distinct, len_pizza_1, len_pizza_2]
            
    
    return pairs
    
def twos_list(pizza_dict):

    num_pizza = len(pizza_dict.keys())
    pairs = []
    
    for i in range(num_pizza):
        for j in range(i):
        
            len_pizza_1 = len(pizza_dict[i])
            len_pizza_2 = len(pizza_dict[j])
            distinct = len(set(pizza_dict[i] + pizza_dict[j]))
            pairs.append([j, i, distinct, len_pizza_1, len_pizza_2])
            
    
    return pairs
        

def threes(pizza_dict):

    num_pizza = len(pizza_dict.keys())
    pairs = {}
    
    for i in range(num_pizza):
        for j in range(i):
            for k in range(j):
                len_pizza_1 = len(pizza_dict[i])
                len_pizza_2 = len(pizza_dict[j])
                len_pizza_3 = len(pizza_dict[k])
                
                distinct = len(set(pizza_dict[i] + pizza_dict[j] + pizza_dict[k]))
                pairs[(k,j,i)] = [distinct, len_pizza_1, len_pizza_2, len_pizza_3]
            
    
    return pairs
    

def fours(pizza_dict):

    num_pizza = len(pizza_dict.keys())
    pairs = {}
    
    for i in range(num_pizza):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    len_pizza_1 = len(pizza_dict[i])
                    len_pizza_2 = len(pizza_dict[j])
                    len_pizza_3 = len(pizza_dict[k])
                    len_pizza_4 = len(pizza_dict[l])
                    
                    distinct = len(set(pizza_dict[i] + pizza_dict[j] + pizza_dict[k] + pizza_dict[l]))
                    pairs[(l,k,j,i)] = [distinct, len_pizza_1, len_pizza_2, len_pizza_3, len_pizza_4]
            
    
    return pairs
