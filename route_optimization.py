import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  # Assuming undirected graph
    
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
    
    def shortest_paths_to_charging_stations(self, start, charging_stations):
        distances = self.dijkstra(start)
        shortest_paths = {}
        for station in charging_stations:
            shortest_paths[station] = distances.get(station, "Not reachable")
        return shortest_paths
    
    def recommend_route(self, start, charging_stations):
        shortest_paths = self.shortest_paths_to_charging_stations(start, charging_stations)
        recommended_station = min(shortest_paths, key=shortest_paths.get)
        return recommended_station, shortest_paths[recommended_station]

def load_network(filename):
    graph = Graph()
    charging_stations = set()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            node = parts[0]
            if '*' in node:
                charging_stations.add(node.replace('*', ''))
                node = node.replace('*', '')
            graph.add_node(node)
            for i in range(1, len(parts), 2):
                neighbor = parts[i]
                weight = int(parts[i + 1])
                graph.add_edge(node, neighbor, weight)
    return graph, charging_stations

# Load the network from the file
network, charging_stations = load_network("network.txt")

# Print the graph in the desired format
print("Node   Connections (with distance)")
for node, neighbors in network.edges.items():
    print(f"{node}      ", end="")
    connections = []
    for neighbor, weight in neighbors.items():
        connections.append(f"{neighbor} ({weight})")
    print(", ".join(connections))

# Define the starting node
starting_node = "A"

# Implement Dijkstra's algorithm to find shortest paths
shortest_paths = network.dijkstra(starting_node)

print("\nShortest paths to charging stations from node", starting_node)
for station in charging_stations:
    print("To charging station", station, ":", shortest_paths.get(station, "Not reachable"))

# Recommend the most efficient route
recommended_station, distance = network.recommend_route(starting_node, charging_stations)
print("\nRecommended charging station:", recommended_station, "with distance:", distance)