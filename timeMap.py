class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)
        self.last_timestamp = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[timestamp][key] = value
        self.last_timestamp = timestamp

    def get(self, key: str, timestamp: int) -> str:
        timestamp = min(timestamp, self.last_timestamp)
        while 0 < timestamp:
            if timestamp in self.timemap and key in self.timemap[timestamp]:
                return self.timemap[timestamp][key]
            timestamp -= 1

        return ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
