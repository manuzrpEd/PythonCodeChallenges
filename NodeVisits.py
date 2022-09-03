# https://www.geeksforgeeks.org/maximum-number-of-nodes-which-can-be-reached-from-each-node-in-a-graph/
# Python3 implementation of the above approach
# Depth First Search
maxx = 100005
graph = [[] for i in range(maxx)]

# Function to perform the DFS calculating the
# count of the elements in a connected component
def dfs(curr, cnt, visited, duringdfs):

	visited[curr] = 1

	# Number of nodes in this component
	cnt += 1
	
	# Stores the nodes which belong
	# to current component
	duringdfs.append(curr)
	
	for child in graph[curr]:

		# If the child is not visited
		if (visited[child] == 0):
			cnt, duringdfs = dfs(child, cnt,
								visited, duringdfs)
	
	return cnt, duringdfs
		
# Function to return the desired
# count for every node in the graph
def MaximumVisit(n, k):

	# To keep track of nodes we visit
	visited = [0 for i in range(maxx)]

	ans = [0 for i in range(maxx)]

	duringdfs = []
	
	for i in range(1, n + 1):
		duringdfs.clear()
		
		cnt = 0

		# If a node is not visited, perform a DFS as
		# this node belongs to a different component
		# which is not yet visited
		if (visited[i] == 0):
			cnt = 0
			cnt, duringdfs = dfs(i, cnt,
								visited, duringdfs)
		
		# Now store the count of all the visited
		# nodes for any particular component.
		for x in duringdfs:
			ans[x] = cnt
			
	# Print the result
	for i in range(1, n + 1):
		print(ans[i], end = ' ')
	
	print()
	
	return

# Function to build the graph
def MakeGraph():
	graph[1].append(2)
	graph[2].append(1)
	graph[2].append(3)
	graph[3].append(2)
	graph[3].append(4)
	graph[4].append(3)
	graph[5].append(6)
	graph[6].append(5)
	graph[6].append(7)
	graph[7].append(6)
	graph[5].append(7)
	graph[7].append(5)

# Driver code
if __name__=='__main__':

	N = 7
	K = 6
	
	# Build the graph
	MakeGraph()
	
	MaximumVisit(N, K)

# This code is contributed by rutvik_56
