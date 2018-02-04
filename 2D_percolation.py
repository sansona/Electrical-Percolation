from union_algorithms import WQU_PathCompression
import sys
import random

#argv[1] = #lattice edge length, argv[2] = proprtion of sites closed/insulating
if len(sys.argv) == 3:
    n = int(sys.argv[1])
    if int(sys.argv[2]) > 1:
        p = int(sys.argv[2])/100
    else:
        p = int(sys.argv[2])
else:
    n = int(input('Unit length of lattice edge: '))
    p = int(input('Proportion of insulating sites: '))
    if p > 1:
        p = p/100
    

lattice = WQU_PathCompression(n**2 + 2) #+2 for top & bottom nodes (used later)

#print ('Original lattice array: ' + str(lattice.array))
closed_index = random.sample(range(1, max(lattice.array)), round((n**2)*p)) #randomly choose index of closed sites

for index in closed_index:
    lattice.array[index] = 'X' #used a char to prevent any index clashing, though results in having to include try-excepts for IndexErrors

#print('Modified lattice array: ' + str(lattice.array))

#cut up lattice.array to n sized lists to better determine connectivity between sites
organized_lattice = [lattice.array[i:i+n] for i in range(1, len(lattice.array) - 1, n)] 

#print('Organized lattice: ' + str(organized_lattice))

#connects open/conducting atoms on same horizontal plane
for plane in organized_lattice:
    for atom in plane:
        try:
            current_atom = plane[atom]
            next_atom = plane[atom+1]

            if current_atom == 'X' or next_atom == 'X':
                #save computation time by not connecting closed sites
                continue
            else:
                #note: union applies to the original lattice.array, not the organized_lattice
                lattice.union(current_atom, next_atom)

        except TypeError:
            continue
        except IndexError:
            continue

#connects open/conducting atoms on same vertical plane
for plane in range(len(organized_lattice)):
    for atom in range(len(organized_lattice[plane])):
        try:
            top_atom = organized_lattice[plane][atom]
            bottom_atom = organized_lattice[plane+1][atom]

            if top_atom == 'X' or bottom_atom == 'X':
                continue
            else:
                lattice.union(top_atom, bottom_atom)

        except IndexError:
            continue

#connect top plane and bottom plane to respective imaginary atoms
top_atom = lattice.array[0]
bottom_atom = lattice.array[-1]

for atom in organized_lattice[0]:
    try:
        lattice.union(top_atom, atom)
    except TypeError:
        #to catch organized_lattice['X']
        continue

for atom in organized_lattice[-1]:
    try:
        lattice.union(bottom_atom, atom)
    except TypeError:
        continue

#reduces complexity of testing connectivity of each top plane atom with each bottom plane atom
print(lattice.connected(top_atom, bottom_atom))









