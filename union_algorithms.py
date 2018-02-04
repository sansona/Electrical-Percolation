class QuickUnion(object):
    #simple quickunion implementation - O(n^2)
    def __init__(self, size):
        self.array = [node for node in range(size)]
        self.size = size

    def union(self, node1, node2):
        #function for combining two nodes
        #array[index] == parent of index
        for index in range(len(self.array)):
            if self.array[index] == self.array[node1]: 
                self.array[index] = self.array[node2]
    
    def connected(self, node1, node2):
        #returns boolean of connectivity between two nodes
        while node1 != self.array[node1]: #finds root node
            node1 = self.array[node1]
        root1 = node1

        while node2 != self.array[node2]:
            node2 = self.array[node2]
        root2 = node2

        return root1 == root2


class WeightedQuickUnion(QuickUnion):
    #add weights to quick union to prevent tall trees - O(n)
    def __init__(self, size):
        self.array = [node for node in range(size)]
        self.weight = [node for node in range(size)] #counts number of roots for corresponding node

    def root(self, node):
        while node != self.array[node]:
            node = self.array[node]
        root = node
        return root

    def union(self, node1, node2):
        root1 = self.root(node1)
        root2 = self.root(node2)

        if root1 == root2:
            return

        if self.weight[root1] < self.weight[root2]:
            self.array[root1] = root2
            self.weight[root2] = self.weight[root2] + self.weight[root1] 

        else:
            self.array[root2] = root1
            self.weight[root1] = self.weight[root1] + self.weight[root2]

class WQU_PathCompression(WeightedQuickUnion):
    #attaches root branch to grandparent upon traversing - O(1) in practice
    def root(self, node):
        while node != self.array[node]:
            self.array[node] = self.array[self.array[node]] #attaches branch to grandparent
            node = self.array[node]
        root = node
        return root


