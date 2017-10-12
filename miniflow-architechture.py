# MiniFlow Architecture

class Node(object):
    def __init__(self, inbound_nodes=[]):
        """
        Two lists: one to store references to the inbound nodes,
        and the other to store references to the outbound nodes.
        """
        self.inbound_nodes = inbound_nodes
        self.outbound_nodes = []
        # For each inpund Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        self.value = None

    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and
        store the result in self.value.
        """
        raise NotImplemented

class Input(Node):
    def __init__(self):
        Node.__init__(self)

    def forward(self, value=None):
        if value is not None:
            self.value = value

class Add(Node):
    def __init__(self):
        Node.__init__(self, [x, y])

    def forward(self):
