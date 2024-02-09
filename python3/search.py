"""
Clean search algorithm.
"""
import random


def binary(nums, target):
    left, right = 0, len(nums) - 1
    while right - left > 1:
        mid = (right - left) // 2 + left
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if nums[right] == target:
        return right
    if nums[left] == target:
        return left
    return None


def create_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]


if __name__ == '__main__':
    test_list = sorted(create_list(20, 0, 100))
    idx = random.randint(0, 20)
    found = binary(test_list, test_list[idx])
    print(idx, found)
