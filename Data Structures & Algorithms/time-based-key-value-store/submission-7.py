class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''
        
        # Binary search
        arr = self.d[key]
        print(arr)

        if arr[0][0] > timestamp:
            return ''

        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            print(l, m, r)
            if arr[m][0] == timestamp:
                return arr[m][1]
            if arr[m][0] > timestamp:
                r = m
            else:
                if arr[m + 1][0] <= timestamp:
                    l = m + 1
                else:
                    return arr[m][1]

        return arr[l][1]
