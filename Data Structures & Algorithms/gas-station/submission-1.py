class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        remain = []
        for g, c in zip(gas, cost):
            remain.append(g - c)

        ret, tmp_remain = None, 0
        for i, r in enumerate(remain):
            if r > 0 and tmp_remain >= 0 and ret is not None:
                return ret
            if r > 0:
                ret, tmp_remain = i, r
            else:
                tmp_remain += r

        return ret if tmp_remain >= 0 and ret is not None else len(remain) - 1