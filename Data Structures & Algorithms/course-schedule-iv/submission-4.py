class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        forward = defaultdict(set)
        backward = defaultdict(set)
        outdegree = [0] * numCourses
        for a, b in prerequisites:
            forward[a].add(b)
            backward[b].add(a)
            outdegree[a] += 1

        courses = deque([i for i in range(numCourses) if outdegree[i] == 0])
        while courses:
            b = courses.popleft()
            for a in backward[b]:
                forward[a].update(forward[b])
                outdegree[a] -= 1
                if outdegree[a] == 0:
                    courses.append(a)

        ret = []
        for u, v in queries:
            ret.append(v in forward[u])
        return ret