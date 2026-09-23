from collections import deque


class Graph:
	"""Directed graph using adjacency lists."""

	def __init__(self):
		# adjacency list: node -> list of neighbors
		self.adj = {}

	def add_edge(self, u, v):
		"""Add a directed edge u -> v."""
		self.adj.setdefault(u, []).append(v)
		self.adj.setdefault(v, [])  # ensure v appears in nodes

	def topsort(self):
		"""Return a list with a topological ordering using Kahn's algorithm.

		Raises ValueError if the graph contains a cycle.
		"""
		# compute indegrees
		indegree = {u: 0 for u in self.adj}
		for u in self.adj:
			for v in self.adj[u]:
				indegree[v] = indegree.get(v, 0) + 1

		# start with all nodes of indegree 0
		q = deque([u for u, d in indegree.items() if d == 0])
		order = []

		while q:
			u = q.popleft()
			order.append(u)
			for v in self.adj.get(u, []):
				indegree[v] -= 1
				if indegree[v] == 0:
					q.append(v)

		if len(order) != len(indegree):
			raise ValueError("Graph has at least one cycle; topological sort not possible")

		return order


if __name__ == "__main__":
	# small example
	g = Graph()
	g.add_edge('shirt', 'belt')
	g.add_edge('shirt', 'tie')
	g.add_edge('tie', 'jacket')
	g.add_edge('belt', 'jacket')
	g.add_edge('pants', 'belt')
	print(g.topsort())