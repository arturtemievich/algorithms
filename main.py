from binary_tree_traversal import TreeNode, BinaryTreeTraversal


def binary_tree_traversal_test_cases():
    # example
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))

    binary_tree = BinaryTreeTraversal()

    print("Test: Level Order")  # output: [[1], [2, 3], [4, 5, 6, 7]]
    print(binary_tree.level_order(root=root) == [[1], [2, 3], [4, 5, 6, 7]])
    print(*binary_tree.level_order(root=root))

    print("\nTest: Preorder Traversal")  # output: [1, 2, 4, 5, 3, 6, 7]
    print(binary_tree.preorder_iterative(root=root) == [1, 2, 4, 5, 3, 6, 7])
    print(binary_tree.preorder_iterative(root=root) == binary_tree.preorder_recursive_v1(root=root))
    binary_tree.preorder_recursive_v2(root=root)
    print()
    print(*binary_tree.preorder_iterative(root=root))

    print("\nTest: Inorder Traversal")  # output: [4, 2, 5, 1, 6, 3, 7]
    print(binary_tree.inorder_iterative(root=root) == [4, 2, 5, 1, 6, 3, 7])
    print(binary_tree.inorder_iterative(root=root) == binary_tree.inorder_recursive_v1(root=root))
    binary_tree.inorder_recursive_v2(root=root)
    print()
    print(*binary_tree.inorder_iterative(root=root))

    print("\nTest: Postorder Traversal")  # output: [4, 5, 2, 6, 7, 3, 1]
    print(binary_tree.postorder_recursive_v1(root=root) == [4, 5, 2, 6, 7, 3, 1])
    binary_tree.postorder_recursive_v2(root=root)
    print()
    print(*binary_tree.postorder_recursive_v1(root=root))


def main():
    binary_tree_traversal_test_cases()


if __name__ == "__main__":
    main()
