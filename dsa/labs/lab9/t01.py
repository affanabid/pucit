import random
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.calculateHeight(root.left), self.calculateHeight(root.right))

        root = self.rotation(root, value)
        
        return root

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rotation(self, node, value):
        balanceFactor = self.balance_factor(node)
        # case-1: Left-Left
        if balanceFactor > 1 and value < node.left.value:
            return self.rotation_rr(node)
        
        # case-2: Right Right
        elif balanceFactor < -1 and value > node.right.value:
            return self.rotation_ll(node)
        
        # case-3: Left Right
        elif balanceFactor > 1 and value > node.left.value:
            node.left = self.rotation_ll(node.left)
            return self.rotation_rr(node)
        
        elif balanceFactor < -1 and value < node.right.value:
            node.right = self.rotation_rr(node.right)
            return self.rotation_ll(node)
        
        return node

    def rotation_ll(self, node):
        child = node.right
        temp = child.left
        
        child.left = node
        node.right = temp

        node.height = 1 + max(self.calculateHeight(node.left), self.calculateHeight(node.right))

        child.height = 1 + max(self.calculateHeight(child.left), self.calculateHeight(child.right))

        return child
    
    def rotation_lr(self, node):
        node.left = self.rotation_ll(node.left)
        return self.rotation_rr(node)
    
    def rotation_rr(self, node):
        child = node.left
        temp = child.right

        child.right = node
        node.left = temp

        node.height = 1 + max(self.calculateHeight(node.left), self.calculateHeight(node.right))

        child.height = 1 + max(self.calculateHeight(child.left), self.calculateHeight(child.right))

        return child

    def rotation_rl(self, node):
        node.right = self.rotation_rr(node.right)
        return self.rotation_ll(node)

    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        print(p.value, end=" ")
        if p.right:
            self.inorder(p.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)
    
    def getHeight(self):
        return self.calculateHeight(self.root)

    def calculateHeight(self, root):
        if root is None:
            return 0
        lh = self.calculateHeight(root.left)
        rh = self.calculateHeight(root.right)
        return max(lh, rh) + 1
    
    
tree = AVL()
for _ in range(500):
    val = random.randint(10, 2000)
    tree.insert_value(val)
    print("\n\nHeight:", tree.getHeight())
    print("In Order:\t", end="")
    tree.inorder_traversal()