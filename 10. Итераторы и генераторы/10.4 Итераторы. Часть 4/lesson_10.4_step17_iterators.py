class Xrange:
    def __init__(self, start: int, end: int, step: int | float = 1) -> None:
        self.start = start
        self.end = end
        self.step = step
        self.current = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.step > 0 and self.current >= self.end or self.step < 0 and self.current <= self.end:
            raise StopIteration

        return self.current
