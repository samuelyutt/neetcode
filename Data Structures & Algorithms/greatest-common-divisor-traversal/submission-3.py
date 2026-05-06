class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def get_divisor(val):
            ret = set()
            for i in range(2, val + 1):
                if val % i == 0:
                    ret.add(i)
            return ret

        a = {} # val -> set(divisors)
        b = defaultdict(list) # divisor -> [vals]

        nums = list(set(nums))
        if max(nums) == 1:
            return False

        for val in nums:
            divisors = get_divisor(val)
            a[val] = divisors
            for d in divisors:
                b[d].append(val)

        comm_divisors = set()
        visited = set()
        q = deque([nums[0]])
        while q:
            val = q.popleft()
            visited.add(val)
            divisors = a[val]
            for d in divisors:
                if d not in comm_divisors:
                    comm_divisors.add(d)
                    for v in b[d]:
                        if v not in visited:
                            q.append(v)
        return len(visited) == len(nums)

