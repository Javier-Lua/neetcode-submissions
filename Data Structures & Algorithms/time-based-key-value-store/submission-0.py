class TimeMap:

    ## Important constraint: timestamps are strictly increasing
    ## when they are added to TimeMap -> Use binary search when
    ## running get()
    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            ls = self.store[key]
            ls.append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            ls = self.store[key]
            return self._binary_search(ls, 0, len(ls) - 1, timestamp)
        else:
            return ""

    # ascending order, has at least one element when run
    def _binary_search(self, ls, left, right, timestamp) -> str:
        if left > right:
            return ""
        mid = (left + right) // 2
        if ls[mid][1] == timestamp:
            return ls[mid][0]
        else:
            if ls[mid][1] < timestamp:
                res = self._binary_search(ls, mid + 1, right, timestamp)
                if res == "":
                    return ls[mid][0]
                else:
                    return res
            else:
                # ls[mid][1] > timestamp
                return self._binary_search(ls, left, mid - 1, timestamp)
