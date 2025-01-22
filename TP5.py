import heapq

# Define the graph nodes and edges
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
node_count = len(nodes)
node_index_map = {node: idx for idx, node in enumerate(nodes)}

# Initialize the adjacency matrix with infinity
adjacency_matrix = [[float('inf')] * node_count for _ in range(node_count)]

# Define the edges with weights
edges = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]

# Populate the adjacency matrix
for start, end, weight in edges:
    start_idx, end_idx = node_index_map[start], node_index_map[end]
    adjacency_matrix[start_idx][end_idx] = weight
    adjacency_matrix[end_idx][start_idx] = weight

# Function to print the adjacency matrix
def print_adjacency_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        formatted_row = ["∞" if value == float('inf') else str(value) for value in row]
        print("  ".join(formatted_row))

# Print the adjacency matrix
print_adjacency_matrix(adjacency_matrix)

index_to_node = {idx: node for node, idx in node_index_map.items()}

#Construct Dijkstra function
def dijkstra(adj_matrix, start_node, end_node):
    start_idx = node_index_map[start_node]
    end_idx = node_index_map[end_node]
    
    distances = [float('inf')] * node_count
    distances[start_idx] = 0
    previous_nodes = [None] * node_count
    priority_queue = [(0, start_idx)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor_idx, weight in enumerate(adj_matrix[current_node]):
            if weight != float('inf'): 
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor_idx]:
                    distances[neighbor_idx] = tentative_distance
                    previous_nodes[neighbor_idx] = current_node
                    heapq.heappush(priority_queue, (tentative_distance, neighbor_idx))
    
    # Reconstruct the shortest path
    path = []
    current = end_idx
    while current is not None:
        path.append(index_to_node[current])
        current = previous_nodes[current]
    path.reverse()

    return path, distances[end_idx]

start_node = input("Enter source node (A-M): ").strip().upper()
end_node = input("Enter target node (A-M): ").strip().upper()

if start_node in node_index_map and end_node in node_index_map:
    path, weight = dijkstra(adjacency_matrix, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}")
    print(f"Total weight of the path: {weight}")
else:
    print("Invalid input. Please use valid node labels (A-M)")