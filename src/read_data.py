
def read_data(file_url):

    my_file = open(file_url, "r")

    info_line = [int(x) for x in my_file.readline().strip().split()]

    n_pizza = info_line[0]
    n_T2 = info_line[1]
    n_T3 = info_line[2]
    n_T3 = info_line[3]
    
    pizzas = dict()
    for i in range(n_pizza): 
        line = my_file.readline().strip().split()
        pizzas[i] = line[1:]

    my_file.close

    return n_pizza, n_T2, n_T3, n_T3, pizzas








if __name__ == '__main__':
    url = './data/d_many_pizzas.in'
    n,_,_,_,pizzas_dict = read_data(url)
    print(pizzas_dict[0] )
    print(pizzas_dict[n-5] )

