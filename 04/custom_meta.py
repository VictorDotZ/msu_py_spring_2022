class CustomMeta(type):
    def __new__(cls, __name, __bases, classdict):
        classdict = {
            attr_name
            if attr_name[0:2] == "__" and attr_name[-1:-3:-1] == "__"
            else f"custom_{attr_name}": attr_value
            for attr_name, attr_value in classdict.items()
        }

        if "__setattr__" in classdict:
            setted_setattr = classdict["__setattr__"]

            def helper(self, name, value):
                previous_state = dict(self.__dict__)
                setted_setattr(self, name, value)

                new_attrs = {
                    k: self.__dict__[k]
                    for k in set(self.__dict__) - set(previous_state)
                }

                for attr_name, attr_value in new_attrs.items():
                    object.__delattr__(self, attr_name)
                    object.__setattr__(self, f"custom_{attr_name}", attr_value)

            classdict["__setattr__"] = helper
        else:
            classdict[
                "__setattr__"
            ] = lambda self, name, value: super.__setattr__(
                self, f"custom_{name}", value
            )

        return super().__new__(cls, __name, __bases, classdict)
