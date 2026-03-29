class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_map = defaultdict(list) # src -> [(dst, price)]
        for flight in flights:
            flights_map[flight[0]].append((flight[1], flight[2]))

        prices_map = defaultdict(int) # place -> cur_price
        q = deque([(src, 0, 0)]) # [(place, cur_k, cur_price)]
        while q:
            place, cur_k, cur_price = q.popleft()
            if cur_k > k + 1:
                continue
            if prices_map[place] != 0 and cur_price >= prices_map[place]:
                continue
            prices_map[place] = cur_price
            for next_dst, price in flights_map[place]:
                q.append((next_dst, cur_k + 1, cur_price + price))
        return prices_map[dst] if prices_map[dst] else -1
