from union_algorithms import WQU_PathCompression
import math
import random

#Runs simple Monte Carlo simulation to determine percolation thresshold of 1000 atom 2D lattice

def percolation_threshhold():
    number_atoms = 100 #temporarily 100 for ease of computation
    lattice = WQU_PathCompression(number_atoms + 2) #+2 for placeholder atoms used later to determine connectivity

    lattice.array[1:-1] = ['X' for atom in lattice.array[1:-1]] #all atoms except for placeholders start off insulating

    top_atom = lattice.array[0]
    bottom_atom = lattice.array[-1]

    number_open_sites = -1 #-1 to account for continues in while loop
    conductive = False
    open_index = random.sample(range(1, number_atoms), 98)

    while conductive == False:
        number_open_sites = number_open_sites + 1
        try:
            #defines adjacent atoms if available - else catches in IndexError
            next_atom = lattice.array[open_index[number_open_sites] + 1]
            previous_atom = lattice.array[open_index[number_open_sites] - 1]
            upper_atom = lattice.array[open_index[number_open_sites] - 100]
            lower_atom = lattice.array[open_index[number_open_sites] + 100]
        except IndexError:
            #for when current atom is close to edge cases
            pass

        lattice.array[open_index[number_open_sites]] = open_index[number_open_sites] #random atom becomes conductive
        current_atom = lattice.array[open_index[number_open_sites]]
        
        #connect top placeholder w/ any conductive atom in top plane
        if open_index[number_open_sites] <= math.sqrt(number_atoms):
            lattice.union(top_atom, current_atom)
            
        #same as above but for bottom plane
        if open_index[number_open_sites] >= number_atoms - math.sqrt(number_atoms):
            lattice.union(bottom_atom, current_atom)

        try:
            lattice.union(current_atom, next_atom)
            lattice.union(current_atom, previous_atom)
            lattice.union(current_atom, upper_atom)
            lattice.union(current_atom, lower_atom)
        except UnboundLocalError:
            #for if passed on one of adjacent atoms in earlier try-except
            pass
        except TypeError:
            #for if one of adjacent atoms is still insulating
            pass

        conductive = lattice.connected(top_atom, bottom_atom)

    print('Percent sites conductive for lattice to be conductive: %s' %(number_open_sites/100))
    
    return number_open_sites/100

percolation_threshhold()

#Next: 1. Implement Monte Carlo simulation, 2. Implement graphing to determine threshhold, 3. Include confidence intervals




