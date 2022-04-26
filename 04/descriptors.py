class MinusOneFloat:
    def __init__(self):
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, val):
        if not isinstance(val, float) or val > 0.0 or val < -1.0:
            raise ValueError
        setattr(obj, self.private_name, val)


class String:
    def __init__(self, max_len):
        self.max_len = max_len
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, val):
        if not isinstance(val, str) or len(val) > self.max_len:
            raise ValueError
        setattr(obj, self.private_name, val)


class PositiveInteger:
    def __init__(self):
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, val):
        if not isinstance(val, int) or val <= 0:
            raise ValueError
        setattr(obj, self.private_name, val)
