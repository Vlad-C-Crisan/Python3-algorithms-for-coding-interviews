""" Python3 code for the counting sort algorithm.

The count_sort function takes as input an array and an integer k, and assumes that all elements
in the input array are integers from the set {0,1, ..., k}. The function outputs an array consisting
of the elements of the input array, sorted in ascending order. The time complexity and space complexity
for this function are both O(n+k). Moreover, the algorithm is stable, i.e., equal elements appear in the
output in the same order the appear in the input. This is essential for other algorithms that use counting
sort as a subroutine, for example radix sort. For more details, see Chapter 8.2 from 3rd edition of
Cormen - Introduction to Algorithms.

The file also contains the class TestCountSort, which provides several test cases for the below implementation
of counting sort.
"""

import unittest


def count_sort(arr, k):
    # initialize the array that will track the elements of the input array
    track_array = [0] * (k+1)

    # store in track_array[j] how many elements in arr are equal to j
    n = len(arr)
    for j in range(n):
        track_array[arr[j]] += 1

    # store in track_array[j] how many elements in arr are <= j
    for j in range(1, k+1):
        track_array[j] += track_array[j-1]

    print(track_array)

    # based on the info in track_array, we sort the elements in arr, in a stable way
    sorted_array = [0] * n
    for j in range(n - 1, -1, -1):
        # there are track_array[arr[j]] elements in arr that are <= arr[j], so arr[j] has to occupy this index
        # the -1 comes from the fact that we start indexing from 0
        sorted_array[track_array[arr[j]]-1] = arr[j]

        # decrement the count after placing arr[j] in the right position
        track_array[arr[j]] -= 1

    return sorted_array


class TestCountSort(unittest.TestCase):

    def setUp(self):
        # construct several types of arrays
        self.array_to_sort_1 = [1, 1, 5, 9, 3, 2, 3, 4, 5, 6, 5, 5, 5]
        self.array_to_sort_2 = [1, 3, 5, 7, 9, 11, 13]
        self.array_to_sort_3 = [9, 8, 7]
        self.array_to_sort_4 = []

    def test_random_order(self):
        actual = count_sort(self.array_to_sort_1, 9)
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 9]
        self.assertEqual(actual, expected)

    def test_already_sorted(self):
        actual = count_sort(self.array_to_sort_2, 13)
        expected = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(actual, expected)

    def test_reverse_sorted(self):
        actual = count_sort(self.array_to_sort_3, 9)
        expected = [7, 8, 9]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        actual = count_sort(self.array_to_sort_4, 0)
        expected = []
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
