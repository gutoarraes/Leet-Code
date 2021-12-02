# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                last = mid-1
            elif nums[mid] < target:
                first = mid+1
        return -1