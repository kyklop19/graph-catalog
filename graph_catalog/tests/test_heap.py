import unittest

from graph_catalog.heap import Heap


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap1 = Heap(
            [
                (78, 1),
                (69, 3),
                (23, 2),
                (47, 5),
                (74, 4),
                (74, 6),
                (-90, 7),
                (0, 8),
                (-63, 0),
            ]
        )

    def test_build(self):
        self.heap1.item_list = [
            (-90, 7),
            (-63, 0),
            (23, 2),
            (0, 8),
            (74, 4),
            (74, 6),
            (78, 1),
            (69, 3),
            (47, 5),
        ]

    def test_pop(self):
        res = []
        while len(self.heap1) != 0:
            res.append(self.heap1.pop())

        self.assertEqual(
            res,
            [
                (-90, 7),
                (-63, 0),
                (0, 8),
                (23, 2),
                (47, 5),
                (69, 3),
                (74, 4),
                (74, 6),
                (78, 1),
            ],
        )

    def test_increase_priority(self):
        self.heap1.change_value(-100, 6)
        self.heap1.item_list = [
            (74, 6),
            (-63, 0),
            (-90, 7),
            (0, 8),
            (74, 4),
            (23, 2),
            (78, 1),
            (69, 3),
            (47, 5),
        ]

    def test_decrease_priority(self):
        self.heap1.change_value(100, 4)
        self.heap1.item_list = [
            (-90, 7),
            (-63, 0),
            (23, 2),
            (0, 8),
            (47, 5),
            (74, 6),
            (78, 1),
            (69, 3),
            (74, 4),
        ]


if __name__ == "__main__":
    unittest.main()
