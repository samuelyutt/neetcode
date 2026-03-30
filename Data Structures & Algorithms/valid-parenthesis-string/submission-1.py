class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts, stars = [], []
        for i, c in enumerate(s):
            if c == '(':
                lefts.append(i)
            elif c == '*':
                stars.append(i)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while lefts:
            if len(stars) == 0:
                return False
            i = lefts.pop()
            j = stars.pop()
            if i > j:
                return False
        return True