""" Python3 implementation of the Select algorithm that finds the $k$th smallest element in an array in linear time.

The Select algorithm determines the kth smallest element of an input array of n >= k (distinct) elements in O(n) time.
The below implementation is based on the Select algorithm described in Chapter 9.3 in 3rd edition of
Cormen- Introduction to Algorithms.

The file contains the following functions
    * find_kth_smallest - recursive function that takes as input an array, the value of k, a start index and an
    end index; the function returns the kth smallest element from the elements of the input array lying between
    the input indices. The function is designed to have default arguments, so that it can also be called in the natural
    way by simply giving it as input the array and the value of k. See the implementation and the test cases for more
    details.

    * find_median - auxiliary function used find_kth_smallest that takes as input an array and returns
    the (upper) median in a given array. Within the function find_kth_smallest, this auxiliary function is called only
    on arrays consisting of at most 5 elements, and, therefore, its contribution to the total runtime is constant.

    * partition -  auxiliary function used find_kth_smallest that takes as input an array, a pivot value, start
    and end indices, and partitions the elements of the array that lie between the input indices around the pivot value,
    so that all values less than the pivot value come to the left, and all greater values come
    to the right of the pivot value.

The file also contains the TestQuickSort class, which provides several test cases for the implemented function.

"""


import unittest


def find_median(arr):
    arr.sort()
    median_index = len(arr) // 2 - 1
    return arr[median_index]


def find_kth_smallest(arr, k, start_index=0, end_index=None):
    if k > len(arr):
        return 'The array contains fewer elements than ' + str(k)

    # handle first the case when only arr and k were specified as arguments
    if end_index is None:
        end_index = len(arr)-1

    # determine the length of the array of interest
    n = end_index - start_index + 1

    # create an auxiliary array that will be used for determining the median of medians
    medians_array = [0] * ((n + 4) // 5)

    j = 0
    while j < n // 5:
        medians_array[j] = find_median(arr[start_index+5*j: start_index + 5*j+5])
        j += 1

    if 5*j < n:
        medians_array[j] = find_median(arr[start_index + 5*j:])
        j += 1

    # find the median of medians recursively
    if j == 1:
        # the base case
        median_of_medians = medians_array[0]
    else:
        # the recursive call
        median_of_medians = find_kth_smallest(medians_array, j // 2, 0, j-1)

    # partition the array around the median of medians
    pivot = partition(arr, median_of_medians, start_index, end_index)

    # determine to which side of the pivot to recurse, or if we should exit recursion
    if pivot - start_index == k - 1:
        return arr[pivot]
    elif pivot - start_index < k-1:
        return find_kth_smallest(arr, k - pivot + start_index - 1, pivot + 1, end_index)
    else:
        return find_kth_smallest(arr, k, start_index, pivot-1)


def partition(arr, pivot_value, start_index, end_index):
    j = 0
    while j < len(arr):
        if arr[j] == pivot_value:
            break
        j += 1

    arr[j], arr[end_index] = arr[end_index], arr[j]

    # the below code partitions arr around the element equal to pivot_value
    k = start_index - 1
    for j in range(start_index, end_index):
        if arr[j] <= pivot_value:
            k += 1
            arr[k], arr[j] = arr[j], arr[k]

    # place the pivot_element in the right position in the array and then return its index
    arr[k + 1], arr[end_index] = arr[end_index], arr[k + 1]
    return k + 1


class TestSelect(unittest.TestCase):

    def setUp(self):
        # construct several types of arrays
        self.array_1 = [7, 1, 8, -19, 14, 44, 0.2]
        self.array_2 = [1, 3, 5, 7, 9, 11, 13]
        self.array_3 = [9, 8, 7]
        self.array_4 = []

    def test_random_k(self):
        actual = find_kth_smallest(self.array_1, 4)
        expected = 7
        self.assertEqual(actual, expected)

    def test_smallest_value(self):
        actual = find_kth_smallest(self.array_3, 1)
        expected = 7
        self.assertEqual(actual, expected)

    def test_largest_value(self):
        actual = find_kth_smallest(self.array_2, 7)
        expected = 13
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        actual = find_kth_smallest(self.array_4, 1)
        expected = 'The array contains fewer elements than 1'
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
