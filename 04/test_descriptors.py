import unittest

from descriptors import MinusOneFloat, String, PositiveInteger


class TestDescriptors(unittest.TestCase):
    def setUp(self):
        class Data:  # pylint: disable=too-few-public-methods
            name = String(max_len=10)
            price = PositiveInteger()
            discount = MinusOneFloat()

            def __init__(self, name, price, discount):
                self.name = name
                self.price = price
                self.discount = discount

        self.data_class = Data
        return super().setUp()

    def test_name(self):
        data = self.data_class("pen", 10, -0.1)

        self.assertEqual(data.name, "pen")

        with self.assertRaises(ValueError):
            data.name = "hello world"

        data.name = ""
        self.assertEqual(data.name, "")

        data.name = "0123456789"
        self.assertEqual(data.name, "0123456789")

        with self.assertRaises(ValueError):
            data.name = 50

    def test_price(self):
        data = self.data_class("pen", 10, -0.1)

        self.assertEqual(data.price, 10)

        with self.assertRaises(ValueError):
            data.price = -1

        with self.assertRaises(ValueError):
            data.price = 0

        with self.assertRaises(ValueError):
            data.price = "50"

        data.price = 1
        self.assertEqual(data.price, 1)

        data.price = 500
        self.assertEqual(data.price, 500)

    def test_discount(self):
        data = self.data_class("pen", 10, -0.1)

        self.assertEqual(data.discount, -0.1)

        with self.assertRaises(ValueError):
            data.discount = 0

        with self.assertRaises(ValueError):
            data.discount = -1.1

        with self.assertRaises(ValueError):
            data.discount = 0.1
        with self.assertRaises(ValueError):
            data.discount = "50"

        data.discount = 0.0
        self.assertEqual(data.discount, 0.0)

        data.discount = -0.5
        self.assertEqual(data.discount, -0.5)


if __name__ == "__main__":
    unittest.main()
