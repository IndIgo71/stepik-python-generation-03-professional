class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.times:
            self.count += 1
            return self.obj
        else:
            raise StopIteration
