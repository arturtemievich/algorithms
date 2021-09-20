from binary_tree_traversal import TreeNode, BinaryTreeTraversal
from searching import linear_search, binary_search, binary_search_recursively, GraphSearch
from array import get_maximum_subarray_sum


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


def search_test_cases():
    # example
    array = [1, 2, 3, 4, 5, 6, 7]
    n = len(array)
    for x in [1, 4, 7, 0]:
        print(linear_search(array=array, x=x) == x - 1,
              binary_search(array=array, left=0, right=n - 1, x=x) == x - 1,
              binary_search_recursively(array=array, left=0, right=n - 1, x=x) == x - 1)


def graph_search_test_cases():
    # example
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'C'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    graph_search = GraphSearch()
    graph_search.breadth_first_search(graph, 'A')
    print()
    graph_search = GraphSearch()
    graph_search.depth_first_search(graph, 'A')
    print()


def maximum_subarray_sum_test_cases():
    # Kadane's algorithm
    case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # output: 6
    case_2 = [1]                              # output: 1
    case_3 = [5, 4, -1, 7, 8]                 # output: 23

    print(get_maximum_subarray_sum(case_1) == 6)
    print(get_maximum_subarray_sum(case_2) == 1)
    print(get_maximum_subarray_sum(case_3) == 23)


def main():
    test_cases = (binary_tree_traversal_test_cases,
                  search_test_cases,
                  graph_search_test_cases,
                  maximum_subarray_sum_test_cases)

    for test_case in test_cases:
        print(test_case.__name__)
        test_case()
        print()


if __name__ == "__main__":
    main()
