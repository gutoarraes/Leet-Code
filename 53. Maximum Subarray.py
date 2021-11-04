# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = float('-inf')
        best_sum = float('-inf')
        for i in nums:
            current_sum = max(i, current_sum+i)
            best_sum = max(best_sum, current_sum)        
        return best_sum
        