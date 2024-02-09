"""
Clean implementation of the sorting algorithms.
"""
from collections import deque
import random


def selection(nums):
    """Time O(n^2)"""
    for i in range(len(nums) - 1):
        lowest, lowest_idx = nums[i], i
        for j in range(i + 1, len(nums)):
            if nums[j] < lowest:
                lowest, lowest_idx = nums[j], j
        nums[i], nums[lowest_idx] = nums[lowest_idx], nums[i]
    return nums


def bubble(nums):
    """Time O(n^2)"""
    done = False
    while not done:
        done = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                done = False
    return nums


def merge(nums):
    """Time O(nlogn)"""

    def combine(left, right):
        # Sort left and right.
        if len(left) > 1:
            mid = len(left) // 2
            left = combine(left[:mid], left[mid:])
        if len(right) > 1:
            mid = len(right) // 2
            right = combine(right[:mid], right[mid:])
        combined = []
        lptr, rptr = 0, 0
        while lptr < len(left) or rptr < len(right):
            if lptr < len(left) and rptr < len(right):
                if left[lptr] < right[rptr]:
                    combined.append(left[lptr])
                    lptr += 1
                else:
                    combined.append(right[rptr])
                    rptr += 1
            elif lptr < len(left):
                combined.append(left[lptr])
                lptr += 1
            else:
                combined.append(right[rptr])
                rptr += 1
        return combined

    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return combine(nums[:mid], nums[mid:])


def quick(nums):
    if len(nums) <= 1:
        return nums
    subs = deque([(0, len(nums))])
    while len(subs):
        low, high = subs.pop()
        pivot = random.randint(low, high - 1)
        nums[low], nums[pivot] = nums[pivot], nums[low]
        curr = low
        for j in range(low + 1, high):
            if j != curr:
                if nums[j] <= nums[curr]:
                    nums[j], nums[curr] = nums[curr], nums[j]
                    if curr < high - 1:
                        nums[curr + 1], nums[j] = nums[j], nums[curr + 1]
                        curr += 1
        if curr - low > 1:
            subs.append((low, curr))
        if high - (curr + 1) > 1:
            subs.append((curr + 1, high))
    return nums


def create_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]


if __name__ == '__main__':
    test_list = create_list(25, 0, 10)
    ans = sorted(test_list)
    print('=' * 10, 'Selection', '=' * 10)
    print(f'Passed: {ans == selection(list(test_list))}')
    print('=' * 30)
    print('=' * 10, 'Bubble', '=' * 10)
    print(f'Passed: {ans == bubble(list(test_list))}')
    print('=' * 30)
    print('=' * 10, 'Merge', '=' * 10)
    print(f'Passed: {ans == merge(list(test_list))}')
    print('=' * 30)
    print('=' * 10, 'Quick', '=' * 10)
    print(f'Passed: {ans == quick(list(test_list))}')
    print('=' * 30)
