class Counter:
    def __init__(self, _min, _max, _num):
        if min > max or num > max or num < min:
            print('Error, wrong numbers passed')
        else:
            self._min = _min
            self._min = _max
            self._min = _num
            if self._num > _max:
                self._num = _max
            if self._num < _min:
                self.num = _min

    def setMax(self, x):
        if self._min > x or self._num > x:
            print('Error, wrong number passed')
        else:
            self._max = x

    def setMin(self, x):
        if x > self._max or self._num < x:
            print('Error, wrong number passed')
        else:
            self._min = x

    def add(self):
        if self._num + 1 > self._max:
            print('Error, counter overflow')
        else:
            self._num += 1

    def showcurrent(self):
        return self._num