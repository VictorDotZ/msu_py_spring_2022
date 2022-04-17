class CustomList(list):
    def __init__(self, data=None):
        super().__init__()
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, i, value):
        self._data[i] = value

    def __str__(self):
        return f"{sum(self._data)}:\t{str(self._data)}"

    def __apply_elementwise(self, other, operator="+"):
        out = []
        min_len = min(len(self), len(other))
        for i in range(min_len):
            if operator == "+":
                out.append(self[i] + other[i])
            elif operator == "-":
                out.append(self[i] - other[i])
        if len(self) < len(other):
            out += other[min_len:]
        else:
            out += self[min_len:]
        return CustomList(out)

    def __add__(self, other):
        return self.__apply_elementwise(other, "+")

    def __sub__(self, other):
        return self.__apply_elementwise(other, "-")

    def __lt__(self, other):
        return sum(self[0:]) < sum(other[0:])

    def __le__(self, other):
        return not self > other

    def __eq__(self, other):
        return sum(self[0:]) == sum(other[0:])

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return sum(self[0:]) > sum(other[0:])

    def __ge__(self, other):
        return not self < other
