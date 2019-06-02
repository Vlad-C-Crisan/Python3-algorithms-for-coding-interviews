""" Python3 code for the merge sort procedure.

The running time of the function for an array of size n is O(n*log(n)). For a proof of this fact, see for
example Chapter 2 in 3rd edition of Cormen - Introduction to Algorithms.

The additional space that merge sort needs for the below (not in place) implementation is O(n)-see for
example https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity

The file contains the following functions
    * merge_sort - recursive function that takes as input an array, a start index and an end index,
    and sorts the input array between the two given indices (inclusive) in ascending order. The function
    is designed to have default arguments, so that it can also be called in the natural way, by giving it
    only the array as input, when we want to sort the entire array.

    * merge - auxiliary function used by merge_sort; it takes as input an array and three indices
    start, middle, end and assumes that the input array is sorted in ascending order
    between start and middle (inclusive) and between middle and end (inclusive), respectively; the
    function returns an array containing all elements between start and end of the input array, sorted in
    ascending order.

The file also contains the TestMergeSort class, which provides several test cases for the implemented function.
"""

import unittest


def merge_sort(arr, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(arr) - 1

    if start_index < end_index:
        middle_index = (start_index + end_index) // 2
        merge_sort(arr, start_index, middle_index)
        merge_sort(arr, middle_index + 1, end_index)
        merge(arr, start_index, middle_index, end_index)


def merge(arr, start_index, middle_index, end_index):
    # calculate first the sizes of arr[start_index: middle_index] and arr[middle_index+1:]
    left_size = (middle_index - start_index + 1)
    right_size = (end_index - middle_index)

    # initialize the left and right arrays
    left_array = [0] * left_size
    right_array = [0] * right_size

    # copy the elements of the input array in the auxiliary left and right arrays
    for i in range(left_size):
        left_array[i] = arr[start_index + i]

    for j in range(right_size):
        right_array[j] = arr[middle_index+j+1]

    # put all the elements back into the input array, in ascending order
    left_counter = 0
    right_counter = 0
    array_counter = start_index

    while (left_counter < left_size) and (right_counter < right_size):
        if left_array[left_counter] <= right_array[right_counter]:
            arr[array_counter] = left_array[left_counter]
            left_counter += 1
        else:
            arr[array_counter] = right_array[right_counter]
            right_counter += 1
        array_counter += 1

    # copy any potentially remaining elements in the left_array at the end of the above while
    while left_counter < left_size:
        arr[array_counter] = left_array[left_counter]
        left_counter += 1
        array_counter += 1

    # copy any potentially remaining elements in the right_array
    while right_counter < right_size:
        arr[array_counter] = right_array[right_counter]
        right_counter += 1
        array_counter += 1

    return arr


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        # construct several types of arrays
        self.array_to_sort_1 = [7, 1, 8, -19, 14, 44, 0.2]
        self.array_to_sort_2 = [1, 3, 5, 7, 9, 11, 13]
        self.array_to_sort_3 = [9, 8, 7]
        self.array_to_sort_4 = []

    def test_random_order(self):
        merge_sort(self.array_to_sort_1, 0, len(self.array_to_sort_1)-1)
        actual = self.array_to_sort_1
        expected = [-19, 0.2, 1, 7, 8, 14, 44]
        self.assertEqual(actual, expected)

    def test_already_sorted(self):
        merge_sort(self.array_to_sort_2, 0, len(self.array_to_sort_2)-1)
        actual = self.array_to_sort_2
        expected = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(actual, expected)

    def test_reverse_sorted(self):
        merge_sort(self.array_to_sort_3, 0, len(self.array_to_sort_3)-1)
        actual = self.array_to_sort_3
        expected = [7, 8, 9]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        merge_sort(self.array_to_sort_4, 0, len(self.array_to_sort_4) - 1)
        actual = self.array_to_sort_4
        expected = []
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
