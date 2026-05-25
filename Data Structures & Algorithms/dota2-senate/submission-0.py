class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        r = d = -1
        for i in range(len(senate)):
            if r == -1 and senate[i] == 'R':
                r = i
            if d == -1 and senate[i] == 'D':
                d = i

        i = 0
        while(r != -1 and d != -1):
            # round
            cur = senate[i]
            if cur == 'R':
                r += 1
                senate[d] = 'X'
            elif cur == 'D':
                d += 1
                senate[r] = 'X'
            senate.append(cur)

            # find next r and d
            while (r < len(senate) and senate[r] != 'R'):
                r += 1
            if r == len(senate):
                r = -1

            while (d < len(senate) and senate[d] != 'D'):
                d += 1
            if d == len(senate):
                d = -1

            i += 1

        return 'Radiant' if d == -1 else 'Dire'
