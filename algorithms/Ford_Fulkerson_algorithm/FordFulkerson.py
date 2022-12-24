# Python program for implementation of Ford Fulkerson algorithm
from BFS import BFS

# This class represents a directed graph using adjacency matrix representation
class Graph:
	def __init__(self, graph: list):
		self.graph: list = graph # residual graph
		self.ROW: int = len(graph)
	
# Returns the maximum flow from s to t in the given graph
def FordFulkerson(g: Graph, source: int, terminal: int) -> int:

	# This array is filled by BFS and to store path
	parent = [-1]*(g.ROW)

	max_flow = 0

	# Augment the flow while there is path from source to terminal
	while BFS(g.graph, source, terminal, parent) :

		# Find the maximum flow through the path found.
		path_flow = float("Inf")
		s = terminal
		while(s != source):
			path_flow = min(path_flow, g.graph[parent[s]][s])
			s = parent[s]

		# Add path flow to overall flow
		max_flow += path_flow

		# update residual capacities of the edges and reverse edges along the path
		v = terminal
		while(v != source):
			u = parent[v]
			g.graph[u][v] -= path_flow
			g.graph[v][u] += path_flow
			v = parent[v]

	return max_flow


# Create a graph given in the above diagram
graph = [
    [0, 16, 13,  0,  0,  0],
    [0,  0, 10, 12,  0,  0],
    [0,  4,  0,  0, 14,  0],
    [0,  0,  9,  0,  0, 20],
    [0,  0,  0,  7,  0,  4],
    [0,  0,  0,  0,  0,  0]
]

g = Graph(graph)

source = 0; terminal = 5

print ("The maximum possible flow is %d " % FordFulkerson(g, source, terminal))

