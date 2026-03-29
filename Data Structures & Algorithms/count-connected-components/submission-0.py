class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = {i: set([i]) for i in range(n)}

        for edge in edges:
            a, b = edge[0], edge[1]
            if a == b:
                continue
            
            i, j = 0, 0
            while i not in components or a not in components[i]:
                i += 1
            while j not in components or b not in components[j]:
                j += 1
            
            if i == j:
                continue
            else:
                components[i].update(components[j])
                del components[j]

        return len(components)
