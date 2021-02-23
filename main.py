from src import bests, read_data, deliveries


import pandas as pd


def main_function(url):

    n_pizza, t2, t3, t4, pizza_dict = read_data.read_data(url)

    print(t2,t3,t4)

    our_orders = deliveries.Orders()

    pairs = bests.twos_list(pizza_dict)
    df = pd.DataFrame(columns=['i', 'j', 'n_distinct', 'n_repeating'], data=pairs)
    t2_deliveries, pizza_used = our_orders.assign_t2_deliveries(df, t2)

    for pizza in pizza_used:
        del pizza_dict[pizza]
    
    print('first bit done')
    triplets = bests.threes_list(pizza_dict)
    df = pd.DataFrame(columns=['i', 'j', 'k', 'n_distinct', 'n_repeating'], data=triplets)
    t3_deliveries, pizza_used = our_orders.assign_t3_deliveries(df, t3)
    
    for pizza in pizza_used:
        del pizza_dict[pizza]
    print('send bit done')

    quadruplets = bests.fours_list(pizza_dict)
    df = pd.DataFrame(columns=['i', 'j', 'k', 'l', 'n_distinct', 'n_repeating'], data=quadruplets)
    t4_deliveries, pizza_used = our_orders.assign_t4_deliveries(df, t4)

    return t2_deliveries, t3_deliveries, t4_deliveries


if __name__ == '__main__':
    url = 'data/b_little_bit_of_everything.in'
    d1, d2 = main_function(url)

    print(d1)
    print(d2)



