from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		def bfs(start, adj, visited):
            visited[start] = 1
            queue = deque([ (start, -1) ])
            while queue:
                node, parent = queue.popleft()
                
                for adjNode in adj[node]:
                    if visited[adjNode] == 0:
                        visited[adjNode] = 1
                        queue.append((adjNode, node))
                    elif parent != adjNode:
                        return True
                        
            return False
            
        visited = [0]*V
        for i in range(v):
            if visited[i] == 0:
                if bfs(i, adj, visited):
                    return True
                    
        return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends