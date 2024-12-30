from collections import defaultdict, deque


if __name__ == "__main__":

    def reverse_graph(matrix):
        """Reverse the edges of the graph."""
        n = len(matrix)
        reversed_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    reversed_matrix[j][i] = 1
        return reversed_matrix

    def dfs(matrix, node, visited, stack=None):
        """Perform a DFS and optionally record nodes in a stack."""
        visited[node] = True
        for neighbor in range(len(matrix)):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(matrix, neighbor, visited, stack)
        if stack is not None:
            stack.append(node)

    def kosaraju(matrix):
        """Find the number of strongly connected components using Kosaraju's algorithm."""
        n = len(matrix)
        visited = [False] * n
        stack = []

        # Step 1: Perform DFS to fill the stack with finishing times
        for i in range(n):
            if not visited[i]:
                dfs(matrix, i, visited, stack)

        # Step 2: Reverse the graph
        reversed_matrix = reverse_graph(matrix)

        # Step 3: Perform DFS on the reversed graph in the order of the stack
        visited = [False] * n
        scc_count = 0

        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs(reversed_matrix, node, visited)
                scc_count += 1

        return scc_count

    def bfs(matrix, start, visited):
        """Perform BFS to find all reachable nodes."""
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in range(len(matrix)):
                if matrix[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def count_weakly_connected_components(matrix):
        """Find the number of weakly connected components."""
        n = len(matrix)

        # Convert directed graph to an undirected graph
        undirected_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1 or matrix[j][i] == 1:
                    undirected_matrix[i][j] = 1
                    undirected_matrix[j][i] = 1

        visited = [False] * n
        wcc_count = 0

        for i in range(n):
            if not visited[i]:
                bfs(undirected_matrix, i, visited)
                wcc_count += 1

        return wcc_count

    # Example matrix
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Find the number of strongly and weakly connected components
    scc_count = kosaraju(G)
    wcc_count = count_weakly_connected_components(G)

    print("Number of strongly connected components:", scc_count)
    print("Number of weakly connected components:", wcc_count)

        