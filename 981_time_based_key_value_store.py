class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.store[key]) == 0 or self.store[key][0][0] > timestamp:
            return ""

        l, r = 0, len(self.store[key]) - 1

        while l <= r:
            m = l + (r - l)//2

            if self.store[key][m][0] == timestamp:
                return self.store[key][m][1]
            elif self.store[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        # When the loop ends, l > r.
        # r now points to the largest timestamp <= the given timestamp
        return self.store[key][r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
