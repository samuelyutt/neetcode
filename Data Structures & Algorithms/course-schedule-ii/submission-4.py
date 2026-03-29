class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {}
        for i in range(numCourses):
            d[i] = set()
        for pre in prerequisites:
            before, after = pre[1], pre[0]
            d[after].add(before)
        ret = []
        while d:
            take = []
            for course, befores in d.items():
                if len(befores) == 0:
                    take.append(course)
            if len(take) == 0:
                return []
            ret += take
            for t in take:
                del d[t]
            for course in d:
                for t in take:
                    d[course].discard(t)
        return ret