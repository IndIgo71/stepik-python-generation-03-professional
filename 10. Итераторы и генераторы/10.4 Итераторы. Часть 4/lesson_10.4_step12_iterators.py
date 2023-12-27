class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.keys = tuple(self.data)
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.keys):
            raise StopIteration

        return self.keys[self.counter], self.data[self.keys[self.counter]]
