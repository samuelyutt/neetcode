class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(h)
        ret = ''

        while h:
            neg_cnt, char = heapq.heappop(h)
            tmp = None
            if len(ret) >= 2 and ret[-2:] == f'{char}{char}':
                # pop next one
                tmp = neg_cnt, char
                if h:
                    neg_cnt, char = heapq.heappop(h)
                else:
                    break
            if neg_cnt == 0:
                break
            ret += char
            neg_cnt += 1
            heapq.heappush(h, (neg_cnt, char))
            if tmp:
                heapq.heappush(h, tmp)

        return ret
