#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    res = []
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        vis=set()
        queue=[0]
        path=[]
        
        while queue:
            s=queue.pop(0)
            if s not in vis:
                vis.add(s)
                path.append(s)
                
            neigh=adj[s]
            for n in neigh:
                if n not in vis:
                    queue.append(n)
        return path