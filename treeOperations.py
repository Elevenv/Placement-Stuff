class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.data = item

class Tree:

    def __init__(self):
        self.ino = []
        self.pre = []
        self.post = []

    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)

        if data<node.data:
            node.left = self.insert(node.left, data)

        else:
            node.right = self.insert(node.right, data)
        return node

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.ino.append(root.data)
            self.inorder(root.right)
        return self.ino

    def preorder(self,root):
        if root:
            self.pre.append(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
        return self.pre

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.post.append(root.data)
        return self.post

if __name__=='__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)

    tree = Tree()
    root = tree.createNode(5)
    tree.insert(root, 2)
    tree.insert(root, 10)
    tree.insert(root, 7)
    tree.insert(root, 15)
    tree.insert(root, 12)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 6)
    tree.insert(root, 8)

    print('Inorder : ',tree.inorder(root)) 
    print('Preorder : ',tree.preorder(root))
    print('Postorder : ',tree.postorder(root))
