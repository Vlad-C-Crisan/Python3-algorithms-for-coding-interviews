""" Python3 code for the randomized version of the quick sort procedure.

The expected running time of the function for an array of size n is O(n*log(n)). For a proof of this fact, see for
example Chapter 7 in 3rd edition of Cormen - Introduction to Algorithms.

Quick sort procedure is an in place procedure, and the only additional space complexity comes from the recursive calls,
which can be made to be O(log(n)) in the worst case, using Sedgewick's trick to limit the recursive calls. See
https://en.wikipedia.org/wiki/Quicksort#Space_complexity for more details.

The file contains the following functions
    * quick_sort - recursive function that takes as input an array, a start index and an end index,
    and sorts the input array between the two given indices (inclusive) in ascending order. The function is designed
    to have default arguments, so that it can also be called in the natural way by simply giving it only the array as
    input, when we want to sort the entire array.

    * randomized_partition - auxiliary function used by quick_sort; it takes as input an array and two indices
    start_index, and end_index; it selects a random element (pivot) of the array that lies between the two input
    indices and returns the array partitioned around the pivot, with all elements that are <= pivot lying to the
    left of the pivot and all elements >pivot lying to the right of the pivot

The file also contains the TestQuickSort class, which provides several test cases for the implemented function.
"""


import random
import unittest


def quick_sort(arr, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(arr)-1

    if start_index < end_index:
        partition_index = randomized_partition(arr, start_index, end_index)
        quick_sort(arr, start_index, partition_index - 1)
        quick_sort(arr, partition_index + 1, end_index)


def randomized_partition(arr, start_index, end_index):
    # generate a random pivot
    pivot = random.randint(start_index, end_index)
    arr[pivot], arr[end_index] = arr[end_index], arr[pivot]

    # partition the input array around the pivot
    pivot_element = arr[end_index]
    k = start_index - 1

    # the below code puts all elements <= pivot_element to the left of the pivot_element \
    # and elements > pivot_element to the right of the pivot_element
    for j in range(start_index, end_index):
        if arr[j] <= pivot_element:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]

    # place the pivot_element in the right position in the array and then return its index
    arr[k+1], arr[end_index] = arr[end_index], arr[k+1]
    return k+1


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        # construct several types of arrays
        self.array_to_sort_1 = [7, 1, 8, -19, 14, 44, 0.2]
        self.array_to_sort_2 = [1, 3, 5, 7, 9, 11, 13]
        self.array_to_sort_3 = [9, 8, 7]
        self.array_to_sort_4 = []

    def test_random_order(self):
        quick_sort(self.array_to_sort_1, 0, len(self.array_to_sort_1)-1)
        actual = self.array_to_sort_1
        expected = [-19, 0.2, 1, 7, 8, 14, 44]
        self.assertEqual(actual, expected)

    def test_already_sorted(self):
        quick_sort(self.array_to_sort_2, 0, len(self.array_to_sort_2)-1)
        actual = self.array_to_sort_2
        expected = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(actual, expected)

    def test_reverse_sorted(self):
        quick_sort(self.array_to_sort_3, 0, len(self.array_to_sort_3)-1)
        actual = self.array_to_sort_3
        expected = [7, 8, 9]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        quick_sort(self.array_to_sort_4, 0, len(self.array_to_sort_4) - 1)
        actual = self.array_to_sort_4
        expected = []
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
