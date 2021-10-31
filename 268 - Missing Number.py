#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        print(sum(nums))
        print(range(len(nums)+1))
        print(sum(range(len(nums)+1)) - sum(nums))


a = Solution()
a.missingNumber([0,1,5,4,3])
