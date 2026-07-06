class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deg = {i: 0 for i in range(numCourses)}
        d = defaultdict(list)

        # [a, b]: b -> a
        for a, b in prerequisites:
            deg[a] += 1
            d[b].append(a)

        avail = deque()
        for course, val in deg.items():
            if val == 0:
                avail.append(course)
        
        cnt = 0
        while avail:
            cnt += 1
            course = avail.popleft()

            for next_course in d[course]:
                deg[next_course] -= 1
                if deg[next_course] == 0:
                    avail.append(next_course)

        return cnt == numCourses