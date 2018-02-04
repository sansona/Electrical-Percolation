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
    

lattice = WQU_PathCompression(n**2)

#print ('Original lattice array: ' + str(lattice.array))
closed_index = random.sample(range(0, max(lattice.array)), round((n**2)*p)) #randomly choose index of closed sites

for index in closed_index:
    lattice.array[index] = 0

#print('Modified lattice array: ' + str(lattice.array))

#cut up lattice.array to n sized lists to better determine connectivity between sites
organized_lattice = [lattice.array[i:i+n] for i in range(0, len(lattice.array), n)] 

#print(organized_lattice)

#connects open/conducting atoms on same horizontal plane
for plane in organized_lattice:
    for atom in plane:
        try:
            current_atom = plane[atom]
            next_atom = plane[atom+1]

            if current_atom == 0 or next_atom == 0:
                #save computation time by not connecting closed sites
                continue
            else:
                #note: union applies to the original lattice.array, not the organized_lattice
                lattice.union(current_atom, next_atom)

        except IndexError:
            continue

#connects open/conducting atoms on same vertical plane
for plane in range(len(organized_lattice)):
    for atom in range(len(organized_lattice[plane])):
        try:
            top_atom = organized_lattice[plane][atom]
            bottom_atom = organized_lattice[plane+1][atom]

            if top_atom == 0 or bottom_atom == 0:
                continue
            else:
                lattice.union(top_atom, bottom_atom)

        except IndexError:
            continue

#connect top plane and bottom plane to respective imaginary atoms
top_atom = 100000 #large number to prevent collision
bottom_atom = 999999

lattice.array.insert(0, top_atom)
lattice.array.append(bottom_atom)

for atom in organized_lattice[0]:
    try:
        lattice.union(top_atom, atom)
    except IndexError:
        continue
for atom in organized_lattice[-1]:
    try:
        lattice.union(bottom_atom, atom)
    except IndexError:
        continue

lattice.connected(top_atom, bottom_atom)









