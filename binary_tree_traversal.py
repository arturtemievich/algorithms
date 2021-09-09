from typing import Optional, List


class TreeNode:
    """Definition for a binary tree node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeTraversal:
    """
    Binary Tree Traversal
     |
     |-> Breadth-First
     |         |
     |         |-> Level-Order
     |
     |-> Depth-First
     |         |
     |         |-> Preorder:  <root><left><right>
     |         |-> Inorder:   <left><root><right>
     |         |-> Postorder: <left><right><root>
    """
    @staticmethod
    def level_order(root: Optional[TreeNode]) -> List[List[int]]:
        """Binary Tree Level Order Traversal (LeetCode: 102)
        Time Complexity:  O(n)
        Space Complexity: O(n)
        where n - number of nodes in the binary tree.
        """
        if not root:
            return []

        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue:
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result

    @staticmethod
    def preorder_iterative(root: Optional[TreeNode]) -> List[List[int]]:
        """Binary Tree Preorder Traversal (LeetCode: 144)
        Preorder Traversal: <root><left><right>
        Time Complexity:  O(n)
        Space Complexity: O(n)
        where n - number of nodes in the binary tree.
        """
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def preorder_recursive_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return [root.val] + self.preorder_recursive_v1(root.left) + self.preorder_recursive_v1(root.right)

    def preorder_recursive_v2(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root.val, end=" ")
            self.preorder_recursive_v2(root.left)
            self.preorder_recursive_v2(root.right)

    @staticmethod
    def inorder_iterative(root: Optional[TreeNode]) -> List[List[int]]:
        """Binary Tree Inorder Traversal (LeetCode: 94)
        Inorder Traversal: <left><root><right>
        Time Complexity:  O(n)
        Space Complexity: O(n)
        where n - number of nodes in the binary tree.
        """
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def inorder_recursive_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.inorder_recursive_v1(root.left) + [root.val] + self.inorder_recursive_v1(root.right)

    def inorder_recursive_v2(self, root: Optional[TreeNode]) -> None:
        if root:
            self.inorder_recursive_v2(root.left)
            print(root.val, end=" ")
            self.inorder_recursive_v2(root.right)

    def postorder_recursive_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Binary Tree Postorder Traversal (LeetCode: 94)
        Postorder Traversal: <left><right><root>
        Time Complexity:  O(n)
        Space Complexity: O(n)
        where n - number of nodes in the binary tree.
        """
        if not root:
            return []
        return self.postorder_recursive_v1(root.left) + self.postorder_recursive_v1(root.right) + [root.val]

    def postorder_recursive_v2(self, root: Optional[TreeNode]) -> None:
        if root:
            self.postorder_recursive_v2(root.left)
            self.postorder_recursive_v2(root.right)
            print(root.val, end=" ")
