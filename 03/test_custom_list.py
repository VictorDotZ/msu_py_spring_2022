import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def test_subtraction(self):
        list1 = []
        list2 = []
        list3 = []
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 - custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 - list2)[0:], custom_list3[0:])

        list1 = [5]
        list2 = []
        list3 = [5]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 - custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 - list2)[0:], custom_list3[0:])

        list3 = [-5]
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list2 - custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 - list1)[0:], custom_list3[0:])

        list1 = [5]
        list2 = [1]
        list3 = [4]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 - custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 - list2)[0:], custom_list3[0:])

        list3 = [-4]
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list2 - custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 - list1)[0:], custom_list3[0:])

        list1 = [5, 1, 3, 7]
        list2 = [1, 2, 7]
        list3 = [4, -1, -4, 7]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 - custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 - list2)[0:], custom_list3[0:])

        list3 = [-4, 1, 4, -7]
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list2 - custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 - list1)[0:], custom_list3[0:])

    def test_addition(self):
        list1 = []
        list2 = []
        list3 = []
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 + custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 + list2)[0:], custom_list3[0:])

        list1 = [5]
        list2 = []
        list3 = [5]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 + custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 + list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + list1)[0:], custom_list3[0:])

        list1 = [5]
        list2 = [1]
        list3 = [6]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 + custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 + list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + list1)[0:], custom_list3[0:])

        list1 = [5, 1, 3, 7]
        list2 = [1, 2, 7]
        list3 = [6, 3, 10, 7]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)
        custom_list3 = CustomList(list3)

        self.assertEqual((custom_list1 + custom_list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list1 + list2)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + custom_list1)[0:], custom_list3[0:])
        self.assertEqual((custom_list2 + list1)[0:], custom_list3[0:])

    def test_comparison(self):
        list1 = []
        list2 = []
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)

        self.assertTrue(custom_list1 == custom_list2)
        self.assertFalse(custom_list1 < custom_list2)

        list1 = [5]
        list2 = []
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)

        self.assertTrue(custom_list1 != custom_list2)
        self.assertTrue(custom_list1 > custom_list2)

        list1 = [5]
        list2 = [1]
        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)

        self.assertFalse(custom_list1 == custom_list2)
        self.assertFalse(custom_list1 <= custom_list2)

        list1 = [5, 1, 3, 7]
        list2 = [1, 2, 7]

        custom_list1 = CustomList(list1)
        custom_list2 = CustomList(list2)

        self.assertTrue(custom_list1 != custom_list2)
        self.assertTrue(custom_list1 >= custom_list2)

    def test_to_str(self):
        list1 = []
        custom_list1 = CustomList(list1)

        self.assertEqual(f"{sum(list1)}:\t{str(list1)}", str(custom_list1))

        list1 = [5]
        custom_list1 = CustomList(list1)

        self.assertEqual(f"{sum(list1)}:\t{str(list1)}", str(custom_list1))

        list1 = [5, 1, 3, 7]
        custom_list1 = CustomList(list1)

        self.assertEqual(f"{sum(list1)}:\t{str(list1)}", str(custom_list1))


if __name__ == "__main__":
    unittest.main()
