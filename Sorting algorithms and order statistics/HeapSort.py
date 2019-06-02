""" Python3 code for the heap sort procedure.

The running time of the function for an array of size n is O(n*log(n)). For a proof of this fact, see for
example Chapter 6 in 3rd edition of Cormen - Introduction to Algorithms.

While the below implementation of the auxiliary function max_heapify is recursive, this can be easily turned into an
iterative procedure, making the heap_sort procedure have O(1) space complexity.

The file contains the following functions
    * heap_sort - function that takes as input an array and sorts its elements in ascending order

    * max_heapify - auxiliary function used by heap_sort; it takes as input an array, a start_index and a heap_size;
    the function assumes that the input array satisfies the max heap property starting from both left(start_index)
    right(start_index), but that start_index might be smaller than its children, thus violating the max heap property.
    For more details, see Chapter 6.2 in 3rd edition of Cormen - Introduction to Algorithms.

The file also contains the TestHeapSort class, which provides several test cases for the implemented function.
"""

import unittest


def heap_sort(arr):
    n = len(arr)
    for start_index in range(n, -1, -1):
        max_heapify(arr, start_index, n)

    # now one by one sort and extract elements
    for heap_size in range(n-1, 0, -1):
        # move the largest element on the last entry
        arr[0], arr[heap_size] = arr[heap_size], arr[0]

        # leave the last element untouched and repeat for the remaining array
        max_heapify(arr, 0, heap_size)


def max_heapify(arr, start_index, heap_size):
    left_child_index = 2 * start_index + 1
    right_child_index = 2 * start_index + 2

    largest = start_index
    if left_child_index < heap_size and arr[largest] < arr[left_child_index]:
        largest = left_child_index

    if right_child_index < heap_size and arr[largest] < arr[right_child_index]:
        largest = right_child_index

    if largest != start_index:
        arr[start_index], arr[largest] = arr[largest], arr[start_index]
        max_heapify(arr, largest, heap_size)


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        # construct several types of arrays
        self.array_to_sort_1 = [7, 1, 8, -19, 14, 44, 0.2]
        self.array_to_sort_2 = [1, 3, 5, 7, 9, 11, 13]
        self.array_to_sort_3 = [9, 8, 7]
        self.array_to_sort_4 = []

    def test_random_order(self):
        heap_sort(self.array_to_sort_1)
        actual = self.array_to_sort_1
        expected = [-19, 0.2, 1, 7, 8, 14, 44]
        self.assertEqual(actual, expected)

    def test_already_sorted(self):
        heap_sort(self.array_to_sort_2)
        actual = self.array_to_sort_2
        expected = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(actual, expected)

    def test_reverse_sorted(self):
        heap_sort(self.array_to_sort_3)
        actual = self.array_to_sort_3
        expected = [7, 8, 9]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        heap_sort(self.array_to_sort_4)
        actual = self.array_to_sort_4
        expected = []
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
