class Solution:
    def totalNQueens(self, n: int) -> int:
        avails = set([(i, j) for i in range(n) for j in range(n)])
        q = 0

        def search(i):
            nonlocal q

            if q == n:
                return 1
            
            ret = 0

            for j in range(n):
                if (i, j) in avails:
                    # choose (i, j) to be queen
                    q += 1

                    rm = []
                    for idx in range(n):
                        for pos in [
                            (i, idx),
                            (idx, j),
                            (i + idx, j - idx),
                            (i - idx, j - idx),
                            (i + idx, j + idx),
                            (i - idx, j + idx),
                        ]:
                            if pos in avails:
                                avails.remove(pos)
                                rm.append(pos)

                    ret += search(i + 1)

                    q -= 1
                    for pos in rm:
                        avails.add(pos)

            return ret

        return search(0)

