class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        
        ret = 0
        nodes = set([i for i in range(n)])

        while nodes:
            ret += 1
            q = deque([nodes.pop()])
            
            while q:
                i = q.popleft()
                for nei in adj[i]:
                    if nei in nodes:
                        nodes.remove(nei)
                        q.append(nei)

        return ret