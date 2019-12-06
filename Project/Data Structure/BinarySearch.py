class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def findMAx(self, root):
        if not root: return -inf
        max_left = self.findMAx(root.left)
        max_right = self.findMAx(root.right)
        return max(root.val, max_left, max_right)

def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

def insert(root, val):
    if not root: return Node(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__ == "__main__":
    root =  createBST([1,2,3,6,7,8,9])
    inorder(root)