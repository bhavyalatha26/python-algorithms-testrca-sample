class ZigZagIterator:
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = [_ for _ in (v1, v2) if _]

    def next(self):
        """
        :rtype: int
        """
        item = self.queue.pop(0)
        ret = item.pop(0)
        if item:
            self.queue.append(item)
        return ret

    def has_next(self):
        """
        :rtype: bool
        """
        return self.queue is not None
