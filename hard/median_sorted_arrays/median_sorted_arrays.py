from typing import List
import sys

# len(sorted1) + len(sorted2) >= 1
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) < len(nums2):
        shorter = nums1
        longer = nums2
    else:
        shorter = nums2
        longer = nums1

    # Search for partitions
    low = 0
    high = len(shorter) * 2
    while low <= high:
        shorter_mid = (low + high) // 2
        longer_mid = len(shorter) + len(longer) - shorter_mid
        shorter_left = -sys.maxsize - 1 if shorter_mid == 0 else shorter[(shorter_mid - 1) // 2]
        shorter_right = sys.maxsize - 1 if shorter_mid == len(shorter) * 2 else shorter[shorter_mid // 2]
        longer_left = -sys.maxsize - 1 if longer_mid == 0 else longer[(longer_mid - 1) // 2]
        longer_right = sys.maxsize - 1 if longer_mid == len(longer) * 2 else longer[longer_mid // 2]
        if longer_left > shorter_right:
            low = shorter_mid + 1
        elif shorter_left > longer_right:
            high = shorter_mid - 1
        else:
            return (max(shorter_left, longer_left) + min(shorter_right, longer_right)) / 2
    return 0


assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
assert find_median_sorted_arrays([3, 4], [1, 2]) == 2.5
assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5
assert find_median_sorted_arrays([2, 4], [1, 3]) == 2.5
assert find_median_sorted_arrays([2, 2], [2, 2]) == 2
assert find_median_sorted_arrays([2, 2], [2]) == 2
assert find_median_sorted_arrays([2], [2, 2]) == 2
assert find_median_sorted_arrays([1, 2, 3], [4, 5]) == 3
assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3
assert find_median_sorted_arrays([4, 5], [1, 2, 3]) == 3
assert find_median_sorted_arrays([3, 4, 5], [1, 2]) == 3
assert find_median_sorted_arrays([1, 3, 5], [2, 4]) == 3
assert find_median_sorted_arrays([], [2, 3]) == 2.5
