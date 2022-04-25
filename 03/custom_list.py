from functools import total_ordering

from utils import apply_operator


@total_ordering
class CustomList(list):
    __le__ = object.__le__
    __ge__ = object.__ge__
    __gt__ = object.__gt__
    __ne__ = object.__ne__

    def __init__(self, data: list):
        super().__init__()
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def __str__(self):
        return f"{sum(self._data)}:\t{str(self._data)}"

    def __apply_elementwise(self, other, operator="+"):
        out = []
        min_len = min(len(self), len(other))
        for i in range(min_len):
            out.append(apply_operator(self[i], other[i], operator))

        if len(self) > len(other):
            out += [apply_operator(x, 0, operator) for x in self[min_len:]]

        if len(self) < len(other):
            out += [apply_operator(0, x, operator) for x in other[min_len:]]

        return CustomList(out)

    def __add__(self, other):
        return self.__apply_elementwise(other, "+")

    def __sub__(self, other):
        return self.__apply_elementwise(other, "-")

    def __lt__(self, other):
        return sum(self[0:]) < sum(other[0:])

    def __eq__(self, other):
        return sum(self[0:]) == sum(other[0:])
