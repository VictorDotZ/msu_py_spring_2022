import unittest

from custom_meta import CustomMeta


class TestCustomMeta(unittest.TestCase):
    def test_no_setattr(self):
        class CustomClass(metaclass=CustomMeta):
            prop = 123

            @classmethod
            def classmethod(cls, arg):
                return str(arg)

            def __init__(self, value):
                self.value = value

            def method(self, arg):  # pylint: disable=no-self-use
                return arg

        # pylint: disable=no-member,pointless-statement

        with self.assertRaises(AttributeError) as manager:
            CustomClass.prop

        self.assertEqual(
            str(manager.exception),
            "type object 'CustomClass' has no attribute 'prop'",
        )
        self.assertEqual(CustomClass.custom_prop, 123)

        with self.assertRaises(AttributeError) as manager:
            CustomClass.classmethod(5)

        self.assertEqual(
            str(manager.exception),
            "type object 'CustomClass' has no attribute 'classmethod'",
        )

        self.assertEqual(CustomClass.custom_classmethod(10), "10")

        instance = CustomClass(55)

        with self.assertRaises(AttributeError) as manager:
            instance.value

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'value'",
        )

        self.assertEqual(instance.custom_value, 55)

        with self.assertRaises(AttributeError) as manager:
            instance.method(20)

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'method'",
        )

        self.assertEqual(instance.custom_method(44), 44)

        instance.dynamic = 88  # pylint: disable=attribute-defined-outside-init
        with self.assertRaises(AttributeError) as manager:
            instance.dynamic

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'dynamic'",
        )

        self.assertEqual(instance.custom_dynamic, 88)

    def test_setattr(self):
        # pylint: disable=too-few-public-methods
        class CustomClass(metaclass=CustomMeta):
            def __init__(self, value):
                self.value = value

            def __setattr__(self, __name, __value):
                super().__setattr__(__name, __value)
                super().__setattr__(f"extended_{__name}", __value + 1)

        instance = CustomClass(55)
        # pylint: disable=no-member,pointless-statement

        with self.assertRaises(AttributeError) as manager:
            instance.value

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'value'",
        )

        with self.assertRaises(AttributeError) as manager:
            instance.extended_value

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'extended_value'",
        )

        self.assertEqual(instance.custom_value, 55)
        self.assertEqual(instance.custom_extended_value, 56)

        instance.dynamic = 88  # pylint: disable=attribute-defined-outside-init

        with self.assertRaises(AttributeError) as manager:
            instance.dynamic

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'dynamic'",
        )

        with self.assertRaises(AttributeError) as manager:
            instance.extended_dynamic

        self.assertEqual(
            str(manager.exception),
            "'CustomClass' object has no attribute 'extended_dynamic'",
        )

        self.assertEqual(instance.custom_dynamic, 88)
        self.assertEqual(instance.custom_extended_dynamic, 89)


if __name__ == "__main__":
    unittest.main()
