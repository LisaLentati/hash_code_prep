class Orders():
    def __init__(self,): 
        self.df = None
        self.working_df = None
        self.i_rep = 0


    def assign_t2_deliveries(self, df, t2): 

        self.df = df

        t2_deliveries = []
        pizza_used = []

        self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

        while len(t2_deliveries) < t2:
            print(len(t2_deliveries))
            the_pair = self.pick_best_pair()

            t2_deliveries.append(the_pair)
            pizza_used.append(the_pair[0])
            pizza_used.append(the_pair[1])

            if len(self.working_df) == 0:
                self.i_rep = self.i_rep + 1  

                print(self.i_rep, len(t2_deliveries))

                self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

                mask1 = self.working_df['i'].isin(pizza_used)
                mask2 = self.working_df['j'].isin(pizza_used)
                mask = mask1 | mask2
                self.working_df = self.working_df.loc[~ mask]

        return t2_deliveries, pizza_used

    def assign_t3_deliveries(self, df, t3): 

        self.df = df

        t3_deliveries = []
        pizza_used = []
        
        self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

        while len(t3_deliveries) < t3:
            print(len(t3_deliveries))
            the_triplet = self.pick_best_triplet()

            t3_deliveries.append(the_triplet)
            pizza_used.append(the_triplet[0])
            pizza_used.append(the_triplet[1])
            pizza_used.append(the_triplet[2])

            if len(self.working_df) == 0:
                self.i_rep = self.i_rep + 1  

                print(self.i_rep, len(t3_deliveries))

                self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

                mask1 = self.working_df['i'].isin(pizza_used)
                mask2 = self.working_df['j'].isin(pizza_used)
                mask3 = self.working_df['k'].isin(pizza_used)
                mask = mask1 | mask2 | mask3
                self.working_df = self.working_df.loc[~ mask]

        return t3_deliveries, pizza_used
        
    def assign_t4_deliveries(self, df, t4): 

        self.df = df

        t4_deliveries = []
        pizza_used = []
        
        self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

        while len(t4_deliveries) < t4:
            print(len(t4_deliveries))
            the_quadruplet = self.pick_best_quadruplet()

            t4_deliveries.append(the_quadruplet)
            pizza_used.append(the_quadruplet[0])
            pizza_used.append(the_quadruplet[1])
            pizza_used.append(the_quadruplet[2])
            pizza_used.append(the_quadruplet[3])

            if len(self.working_df) == 0:
                self.i_rep = self.i_rep + 1  

                print(self.i_rep, len(t4_deliveries))

                self.working_df = self.df.loc[self.df['n_repeating']==self.i_rep]

                mask1 = self.working_df['i'].isin(pizza_used)
                mask2 = self.working_df['j'].isin(pizza_used)
                mask3 = self.working_df['k'].isin(pizza_used)
                mask4 = self.working_df['l'].isin(pizza_used)
                mask = mask1 | mask2 | mask3 | mask4
                self.working_df = self.working_df.loc[~ mask]

        return t4_deliveries, pizza_used



    def pick_best_pair(self):
        
        max_val = self.working_df['n_distinct'].max()

        pair = self.working_df[['i', 'j']].loc[self.working_df['n_distinct']==max_val].values[0]

        [i_max, j_max] = pair

        self.working_df = self.working_df[self.working_df['i'] != i_max]
        self.working_df = self.working_df[self.working_df['i'] != j_max]
        self.working_df = self.working_df[self.working_df['j'] != j_max]
        self.working_df = self.working_df[self.working_df['j'] != i_max]

        return list(pair)

    def pick_best_triplet(self):
    
        max_val = self.working_df['n_distinct'].max()

        triplet = self.working_df[['i', 'j', 'k']].loc[self.working_df['n_distinct']==max_val].values[0]

        [i_max, j_max, k_max] = triplet

        self.working_df = self.working_df[self.working_df['i'] != i_max]
        self.working_df = self.working_df[self.working_df['i'] != j_max]
        self.working_df = self.working_df[self.working_df['i'] != k_max]
        self.working_df = self.working_df[self.working_df['j'] != i_max]
        self.working_df = self.working_df[self.working_df['j'] != j_max]
        self.working_df = self.working_df[self.working_df['j'] != k_max]
        self.working_df = self.working_df[self.working_df['k'] != i_max]
        self.working_df = self.working_df[self.working_df['k'] != j_max]
        self.working_df = self.working_df[self.working_df['k'] != k_max]

        return list(triplet)


    def pick_best_quadruplet(self):
    
        max_val = self.working_df['n_distinct'].max()

        quadruplet = self.working_df[['i', 'j', 'k', 'l']].loc[self.working_df['n_distinct']==max_val].values[0]

        [i_max, j_max, k_max, l_max] = quadruplet

        self.working_df = self.working_df[self.working_df['i'] != i_max]
        self.working_df = self.working_df[self.working_df['i'] != j_max]
        self.working_df = self.working_df[self.working_df['i'] != k_max]
        self.working_df = self.working_df[self.working_df['i'] != l_max]
        self.working_df = self.working_df[self.working_df['j'] != i_max]
        self.working_df = self.working_df[self.working_df['j'] != j_max]
        self.working_df = self.working_df[self.working_df['j'] != k_max]
        self.working_df = self.working_df[self.working_df['j'] != l_max]
        self.working_df = self.working_df[self.working_df['k'] != i_max]
        self.working_df = self.working_df[self.working_df['k'] != j_max]
        self.working_df = self.working_df[self.working_df['k'] != k_max]
        self.working_df = self.working_df[self.working_df['k'] != l_max]
        self.working_df = self.working_df[self.working_df['l'] != i_max]
        self.working_df = self.working_df[self.working_df['l'] != j_max]
        self.working_df = self.working_df[self.working_df['l'] != k_max]
        self.working_df = self.working_df[self.working_df['l'] != l_max]

        return list(quadruplet)