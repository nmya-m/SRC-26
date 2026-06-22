state = [1,...,1]
t = 0

max_time = 5; #placeholder for now

#reaction rates
k_plus = 5 ; #placeholder for now
k_minus = 7; #placeholder for now

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

    #UNFINISHED!!
    #PART 2: determine time to next reaction
    '''
    T = random time
    r = random number between 0 and 1

    T = -ln(r)/a_total
    t = t + T
    '''

    #PART 3: determine which reaction occurs