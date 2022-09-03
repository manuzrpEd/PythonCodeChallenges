# https://www.geeksforgeeks.org/maximum-number-of-nodes-which-can-be-reached-from-each-node-in-a-graph/
# Python3 implementation of the above approach
# Depth First Search
# This is the answer to Fitch Exercise (not sure if I have to remove cities visites in subnodes)

# Function to perform the DFS calculating the
# count of the elements in a connected component
def dfs(curr, cnt,cnt_odd, visited, duringdfs):
    visited[curr] = 1
    cnt += 1
    if (curr % 2) != 0:
        cnt_odd +=1
    duringdfs.append(curr)
    for child in graph[curr]:
        if (visited[child] == 0):
            cnt, cnt_odd, duringdfs = dfs(child, cnt,cnt_odd,visited, duringdfs)	
    return cnt, cnt_odd, duringdfs
		
# Function to return the desired
# count for every node in the graph
def MaximumVisit(n, k,graph):
    visited = [0 for i in range(len(graph))]
    ans = [0 for i in range(len(graph))]
    ans_1Odd = [0 for i in range(len(graph))]
    duringdfs = []
    for i in range(1, n):
        duringdfs.clear()
        cnt = 0
        cnt_odd=0
		# If a node is not visited, perform a DFS as
		# this node belongs to a different component
		# which is not yet visited
        if (visited[i] == 0):
            cnt = 0
            cnt_odd = 0
            cnt, cnt_odd, duringdfs = dfs(i, cnt,cnt_odd,visited, duringdfs)
		
		# Now store the count of all the visited
		# nodes for any particular component.
        for x in duringdfs:
            ans[x] = cnt
            ans_1Odd[x] = cnt_odd
			
    print(ans)
    print(ans_1Odd)
    net_odd=[min(n,1) for n in ans_1Odd]
    print(net_odd)
    net_ans=[ans[i]-(ans_1Odd[i]-net_odd[i])+1 for i in range(len(ans))]
    print(net_ans)
	
    print(max(net_ans))
    return

# Function to build the graph
def MakeGraph():
    graph=[[] for val in T]
    for i in range(0,len(T)):
        graph[i].append(T[i])
        for j in range(0,len(T)):
            if T[j]==i:
                graph[i].append(j)
    graph=[list(set(l)) for l in graph]
    for i in range(len(graph)):
        try:
            graph[i].remove(0)
        except:
            pass
    return graph
	
T=[0,9,0,2,6,8,0,8,3,0]
#4
# T=[0,0,0,1,6,1,0,0]
#3
# Driver code
N = len(T)
K = N-1
# Build the graph
graph=MakeGraph()
MaximumVisit(N,K,graph)


