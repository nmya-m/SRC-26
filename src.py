import math
import random
import matplotlib.pyplot as plt
import numpy as np

state = [1] * 20 #list of 20 monomers of length 1
t = 0

max_time = 10; #placeholder for now

trajectory = [(state.copy(), t)]  # store the initial state and time

#reaction rates
k_plus = 5; #placeholder for now
k_minus = 1; #placeholder for now

while t < max_time:
    #PART 1: two reaction types (join or break)
    #join
    n = len(state)
    a_join = k_plus * ((n*(n-1))/2)

    #break
    n_bonds = sum(state[i]-1 for i in range(len(state)))
    a_break = k_minus * n_bonds

    a_total = a_join + a_break

    if a_total == 0: #no more reactions can occur
        break

    #PART 2: determine time to next reaction
    r = random.uniform(0, 1)
    T = -math.log(r)/a_total #random time

    t = t + T
    
    #PART 3: determine which reaction occurs
    f = r * a_total

    if f < a_join:
        #join reaction occurs
        #choose two random indices to join
        i, j = random.sample(range(len(state)), 2)
        state[i] += state[j]
        del state[j]
    else:
        #break reaction occurs
        #choose a random index to break
        bond_index = random.randint(0, n_bonds - 1)
        for i in range(len(state)):
            if bond_index < state[i] - 1:
                #break the bond at index i
                state[i] -= bond_index
                state.append(bond_index)  # add a new monomer of length 1
                break
            else:
                bond_index -= (state[i] - 1)

    trajectory.append((state.copy(), t))    

#PLOT: x-axis: time, y-axis: average polymer length
# the data
x = [trajectory[i][1] for i in range(len(trajectory))]
y = [np.mean(trajectory[i][0]) for i in range(len(trajectory))]

plt.figtext(0.65, 0.75, f"Initial Monomers: {len(trajectory[0][0])}\nK_Plus: {k_plus}\nK_Minus: {k_minus}", fontsize=10, bbox={'facecolor':'orange', 'alpha':0.2})

# create the plot
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Average Polymer Length')

# save the plot as an image
plt.savefig('my_graph.png', dpi=300)

#PLOT: x-axis: polymer length, y-axis: frequency
# the data
avg_lengths = trajectory[(max_time-2)][0] #trajectory at equilibrium (two time steps before the end of the simulation)
plt.figure()
plt.hist(avg_lengths, bins=range(1, max(avg_lengths) + 2), align='left', edgecolor='black')
plt.xlabel('Polymer Length')
plt.ylabel('Frequency')
plt.title('Distribution of Polymer Lengths')
plt.savefig('polymer_lengths.png', dpi=300)
