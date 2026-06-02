class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nei(state):
            a, b, c, d = int(state[0]), int(state[1]), int(state[2]), int(state[3])
            return [
                f'{(a + 1) % 10}{b}{c}{d}',
                f'{a}{(b + 1) % 10}{c}{d}',
                f'{a}{b}{(c + 1) % 10}{d}',
                f'{a}{b}{c}{(d + 1) % 10}',
                f'{(a + 9) % 10}{b}{c}{d}',
                f'{a}{(b + 9) % 10}{c}{d}',
                f'{a}{b}{(c + 9) % 10}{d}',
                f'{a}{b}{c}{(d + 9) % 10}',
            ]

        if '0000' in deadends:
            return -1

        visited = set(deadends)
        q = deque([('0000', 0)])

        while q:
            state, cnt = q.popleft()
            
            # visited.add(state)

            if state == target:
                return cnt

            for next_state in nei(state):
                if next_state not in visited:
                    visited.add(next_state)
                    q.append((next_state, cnt + 1))

        return -1