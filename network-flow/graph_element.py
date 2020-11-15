class Node:
    def __init__(self, index):
        self.index = index
        self.edges = list()
        self.previous_node = None
        self.previous_edge = None

    def __repr__(self):
            return "<%s>" % (self.index)

    def __str__(self):
        return "<%s>" % (self.index)

class Edge:

    def __init__(self, dest1, dest2, cap):
        self.destination1 = dest1  
        self.destination2 = dest2
        self.capacity = cap
        self.flow_front = 0
        self.flow_back = 0

    def is_full(self, node):
        # Check if flow=capacity towards the node 
        if node == self.destination2:
            return self.capacity == self.flow_front
        else:
            return self.capacity == self.flow_back

    def get_capacity(self, node):
        # Returns capacity towards node
        if node == self.destination2:
            return self.capacity - self.flow_front
        else:
            return self.capacity - self.flow_back

    def update_flow(self, node, delta):
        #Increase flow with delta towards node node
        if node == self.destination2:
            self.flow_front += delta
            self.flow_back -= delta
        else:
            self.flow_back += delta
            self.flow_front -= delta
    
    def __repr__(self):
        return "(%s,%s)" % (self.destination1, self.destination2)

    def __str__(self):
        return "(%s,%s)" % (self.destination1, self.destination2)