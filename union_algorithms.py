class QuickUnion(object):
    def __init__(self, size):
        self.array = [node for node in range(size)]
        self.size = size

    def union(self, node1, node2):
        #array[index] == parent of index
        for index in range(len(self.array)):
            if self.array[index] == self.array[node1]:
                self.array[index] = self.array[node2]
    
    def connected(self, node1, node2):
        while node1 != self.array[node1]:
            node1 = self.array[node1]
        root1 = node1

        while node2 != self.array[node2]:
            node2 = self.array[node2]
        root2 = node2
        return root1 == root2


class WeightedQuickUnion(QuickUnion):
    def __init__(self, size):
        self.array = [node for node in range(size)]
        self.weight = [node for node in range(size)]

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

        if weight[root1] < weight[root2]:
            array[root1] = root2
            weight[root2] = weight[root2] + weight[root1]

        else:
            array[root2] = root1
            weight[root1] = weight[root1] + weight[root2]




