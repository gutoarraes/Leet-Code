# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        already = set()
        for i in nums:
            if i in already:
                return True
            else:
                already.add(i)
        return False