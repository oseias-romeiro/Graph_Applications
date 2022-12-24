def BFS(graph: list, s: int, t: int, parent: list) -> bool:

		# Mark all the vertices as not visited
		visited = [False]*(len(graph))

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:
			# Dequeue a vertex from queue
			u = queue.pop(0)

			# Get all adjacent vertices of the dequeued vertex u
			for ind, val in enumerate(graph[u]):
                # If a adjacent has not been visited, then mark it visited and enqueue it
				if visited[ind] == False and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
                    # If reach the terminal vertex
					if ind == t:
						return True

		# If cant reachthe terminal vertex
		return False
        