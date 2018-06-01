class _Leaf:
    
    def __init__(self):
        self.path = list()
        self.idx  = list()
    
    def __add__(self, value):
        self.path.append(value[0])
        self.idx.append(value[1])
        return self


class _Node:
    
    def __init__(self, id, v1, v2):
        self.id = id
        
        self.left  = v1
        self.right = v2
        
        self.left  += (1, id)
        self.right += (-1, id)
    
    def __add__(self, value):
        self.left = self.left + value
        self.right = self.right + value
        return self
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, value):
        self.__left = value
    
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, value):
        self.__right = value
    
    @property
    def leaves(self):
        return self.__leaves
    
    @leaves.setter
    def leaves(self, leaves):
        self.__leaves = leaves

class Tree:
    
    def __init__(self, leaves, h_size, seed=None):
        import numpy as np
        
        if seed:
            np.random.seed(seed)
        
        node_len = len(leaves) - 1
        self.weights = np.random.randn(node_len, h_size)
        
        self._root = self._build_tree(leaves)
    
    def _build_tree(self, leaves):
        self._leaves = {leaf:_Leaf() for leaf in leaves}
        
        leaves = list(self._leaves.values())
        nodes = list()

        id = 0
        while True:
            if len(leaves) > 1:
                node = _Node(id, leaves.pop(), leaves.pop())
                nodes.append(node)
            elif len(nodes) > 1:
                node = _Node(id, nodes.pop(), nodes.pop())
                nodes.insert(0, node)
            else:
                node = _Node(id, nodes.pop(), leaves.pop())
                nodes.append(node)
            
            id += 1
            if len(leaves) == 0 and len(nodes) == 1:
                root = nodes[-1]
                return root
    
    def __getitem__(self, index):
        indexes = self._leaves[index].idx
        return self.weights[indexes]
    
    def get_path(self, index):
        return self._leaves[index].path
    
    def __setitem__(self, index, value):
        indexes = self._leaves[index].idx
        self.weights[indexes] = value