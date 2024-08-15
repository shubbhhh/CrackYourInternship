#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        def dfs(start, adj, visited, pathVisited):
            visited[start] = 1
            pathVisited[start] = 1
            
            for i in adj[start]:
                if visited[i] == 0:
                    if dfs(i, adj, visited, pathVisited):
                        return True
                elif pathVisited[i]:
                    return True
            
            pathVisited[start] = 0
            return False
        
        visited = [0]*V
        pathVisited = [0]*V
            
        for i in range(V):
            if dfs(i, adj, visited, pathVisited):
                return True
                
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends