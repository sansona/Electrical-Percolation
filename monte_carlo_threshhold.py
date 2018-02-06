from union_algorithms import WQU_PathCompression
import matplotlib.pyplot as plt
import statistics
import math
import random

#Runs simple Monte Carlo simulation to determine percolation thresshold of 10000 atom 2D lattice

def percolation_threshhold():
    number_atoms = 10000 
    lattice = WQU_PathCompression(number_atoms + 2) #+2 for placeholder atoms used later to determine connectivity

    lattice.array[1:-1] = ['X' for atom in lattice.array[1:-1]] #all atoms except for placeholders start off insulating

    top_atom = lattice.array[0]
    bottom_atom = lattice.array[-1]

    number_open_sites = -1 #-1 to account for continues in while loop
    conductive = False
    open_index = random.sample(range(1, number_atoms), 10000 - 2)

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
    
    threshhold = number_open_sites/100
    
    return threshhold


def monte_carlo(num_samples):
    threshhold_list = [] #list of percolation_threshholds from each sample
    for sample in range(num_samples):
        percolation_threshhold()
        threshhold_list.append(percolation_threshhold())
    
    stdev = statistics.stdev(threshhold_list)
    mean = statistics.mean(threshhold_list) #can just do sum(threshhold_list)/len(threshhold_list), but this is more efficient
    
    #95% confidence
    lower_interval = mean - (1.96*stdev)/math.sqrt(num_samples)
    upper_interval = mean + (1.96*stdev)/math.sqrt(num_samples)
   

    #begins plotting section
    histogram = plt.hist(
            threshhold_list, 
            bins=20, 
            color='c',
            edgecolor='k', 
            linewidth=2
            )

    #Plots mean line and confidence interval
    plt.axvline(
            mean,
            color='r',
            linestyle='dashed',
            linewidth=3
            )

    plt.axvline(
            lower_interval,
            color='black',
            linestyle='dashed',
            linewidth=1.5
            )

    plt.axvline(
            upper_interval,
            color='black',
            linestyle='dashed',
            linewidth=1.5
            )


    plt.title("Percolation Threshholds from Monte-Carlo Simulation (n = %s)" %num_samples)
    plt.xlabel("Threshhold (%conductive)")
    plt.ylabel("Probability")

    #plt.show()
    plt.savefig('MonteCarlo%s' %num_samples, bbox_inches='tight')

    print('The average threshhold value for 10000 atoms over %s samples is %.2f, with a confidence interval of [%.2f, %.2f]' 
        %(num_samples, mean, lower_interval, upper_interval))
    

monte_carlo(1000) #adjust for number of sample runs






