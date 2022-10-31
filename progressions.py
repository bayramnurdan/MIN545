class Progression:

    def __init__(self, limit=None):
        self._current = 0
        self._count = 0
        self._limit = limit

    def skip(self, n):
        try:
            for i in range(n):
                self.__next__()
        except StopIteration:
            pass

    def __iter__(self):
        return self

    def __next__(self):
        if self._count > self._limit:
            raise StopIteration()
        else:

            self.update()
            self._count += 1

            return self._current

    def update(self):
        pass


class ArithmeticProgression(Progression):

    def __init__(self, step=1, limit=None):
        super().__init__(limit)  # It has to be the first line in the child __init__
        self._step = step

    def update(self):
        self._current += self._step


class GeometricProgression(Progression):

    def __init__(self, multiplier=2, limit=None):
        super().__init__(limit)
        self._current = 1
        self._multiplier = multiplier

    def update(self):
        self._current *= self._multiplier


class FibonacciProgression(Progression):

    def __init__(self, limit=None):
        super().__init__(limit)
        self._current = 1
        self._oldcurrent = 0

    def update(self):
        if self._count == 0:
            self._current = 0
        elif self._count == 1:
            self._current, self._oldcurrent = 1, 0
        else:
           self._current, self._oldcurrent = self._current + self._oldcurrent, self._current



