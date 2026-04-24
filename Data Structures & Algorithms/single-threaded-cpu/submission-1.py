class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)] # [enqueueTimei, processingTimei, i
        tasks.sort()
        ret = []
        queue = [] # heap: processingTimei, i
        t = 0
        idx = 0
        while len(ret) < len(tasks):
            # add available tasks to queue
            while idx < len(tasks) and tasks[idx][0] <= t:
                task = tasks[idx]
                heapq.heappush(queue, (task[1], task[2]))
                idx += 1

            if not queue:
                # skip if no tasks are ready yet
                t = tasks[idx][0]
                continue
            else:
                # processing
                processingTime, i = heapq.heappop(queue)
                ret.append(i)
                t += processingTime
        return ret

