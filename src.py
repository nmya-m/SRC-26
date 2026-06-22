import math
from random import random


state = [1,...,1]
t = 0

max_time = 5; #placeholder for now

#reaction rates
k_plus = 5 ; #placeholder for now
k_minus = 7; #placeholder for now

#while t < max_time:
    #PART 1: two reaction types (join or break)
    #join
        n = len(state)
        a_join = k_plus * ((n*(n-1))/2)

    #break
        n_bonds = sum(state[i]-1 for i in range(len(state)))
        a_break = k_minus * n_bonds

        a_total = a_join + a_break

        if a_total == 0: #no more reactions can occur
          #  break

    #UNFINISHED!!
    #PART 2: determine time to next reaction

T = -math.log(random.random())/a_total

t = t + T
    

    #PART 3: determine which reaction occurs
    f = random(0,1) * a_total

if f < a_join:
        #join reaction occurs
        #choose two random indices to join
        i, j = random.sample(range(len(state)), 2)
        state[i] += state[j]
        del state[j]
    else:
        #break reaction occurs
        #choose a random index to break
        i = random.choice(range(len(state)))
        if state[i] > 2:
               bonds = state[i] - 1  # number of bonds to break
               random_bond = random.randint(1, bonds)  # choose a bond to break
               state[i] -= random_bond  # break the bond
               state.append(random_bond)  # add the new fragment to the state