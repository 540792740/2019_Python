# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        queue = collections.deque([root])
        tree_list = []
        while queue:
            root = queue.popleft()
            if root != None:
                queue.append(root.left)
                queue.append(root.right)
                tree_list.append(str(root.val))
            else:
                tree_list.append('Null')
        return ' '.join(tree_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        tree_list = data.split(' ')
        head = TreeNode(int(tree_list[0]))
        queue = collections.deque([head])
        index = 1
        while queue:
            root = queue.popleft()
            if tree_list[index] != 'Null':
                root.left = TreeNode(int(tree_list[index]))
                queue.append(root.left)
            index += 1
            if tree_list[index] != 'Null':
                root.right = TreeNode(int(tree_list[index]))
                queue.append(root.right)
            index += 1
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))