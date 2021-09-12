def linear_search(array, x) -> int:
    """Linear Search Algorithm
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1


def binary_search(array: list, left: int, right: int, x) -> int:
    """Binary Search Algorithm (Iterative)
    Time Complexity:  O(log(n))
    Space Complexity: O(1)
    """
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == x:
            return middle
        elif array[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def binary_search_recursively(array: list, left: int, right: int, x) -> int:
    """Binary Search Algorithm (Recursively)
    Time Complexity:  O(log(n))
    Space Complexity: O(log(n)) recursion call stack space!
    """
    if right >= left:
        middle = left + (right - left) // 2
        if array[middle] == x:
            return middle
        elif array[middle] < x:
            return binary_search_recursively(array, middle + 1, right, x)
        else:
            return binary_search_recursively(array, left, middle - 1, x)
    return -1


class GraphSearch:
    """
    1. Breadth First Search (BFS)
    2. Depth First Search (DFS)
    """
    def __init__(self):
        self.visited = set()

    def breadth_first_search(self, graph, node):
        """Breadth First Search Algorithm
        Time Complexity:  O(V + E)
        Space Complexity: O(V)
        where V - number of nodes/vertices, E - number of edges.
        p.s. depending on the input graph, O(E) could be between O(1) and O(V ** 2)!
        """
        self.visited.add(node)
        queue = [node]
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for neighbour in graph[s]:
                if neighbour not in self.visited:
                    self.visited.add(neighbour)
                    queue.append(neighbour)

    def depth_first_search(self, graph, node):
        """Depth First Search Algorithm
        Time Complexity:  O(V + E)
        Space Complexity: O(V)
        where V - number of nodes/vertices, E - number of edges.
        """
        if node not in self.visited:
            print(node, end=" ")
            self.visited.add(node)
            for neighbour in graph[node]:
                self.depth_first_search(graph, neighbour)
