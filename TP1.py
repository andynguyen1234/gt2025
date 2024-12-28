if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        1: [2],
        2: [1, 5],
        5: [2],
        3: [6],
        6: [3, 4, 7],
        7: [4, 6],
        4: [6, 7]
    }

    def is_path_exists(graph, start, end):
        """
        Check if a path exists between start and end nodes in the graph.
        
        :param graph: Dictionary representing the adjacency list of the graph
        :param start: Starting node
        :param end: Ending node
        :return: True if a path exists, False otherwise
        """
        visited = set()
        
        def dfs(node):
            if node == end:
                return True
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(start)

    # User input
    start_node = int(input("Enter the start node: "))
    end_node = int(input("Enter the end node: "))

    # Check if path exists
    if is_path_exists(graph, start_node, end_node):
        print("True")
    else:
        print("False")
