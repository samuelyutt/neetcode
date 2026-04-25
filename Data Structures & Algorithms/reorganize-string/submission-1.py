class Solution:
    def reorganizeString(self, s: str) -> str:
        cnts = {}
        for c in s:
            cnts[c] = cnts.get(c, 0) + 1
        h = [(-cnt, c) for c, cnt in cnts.items()]
        heapq.heapify(h)

        ret = []
        while h:
            # pop the most frequent char
            neg_cnt, c = heapq.heappop(h)
            if not ret or ret[-1] != c:
                # append this char
                ret.append(c)
            else:
                if not h:
                    return ''
                # append next char
                tmp = neg_cnt, c
                neg_cnt, c = heapq.heappop(h)
                ret.append(c)
                heapq.heappush(h, tmp)

            neg_cnt += 1
            if neg_cnt:
                heapq.heappush(h, (neg_cnt, c))

        return ''.join(ret)