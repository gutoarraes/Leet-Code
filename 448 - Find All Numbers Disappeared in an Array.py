        # return array of numbers that are NOT inside array nums

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # return array of numbers that are NOT inside array nums
        solucao = []
        print(nums)
        for i in nums:
            pos = abs(i)-1
            if nums[pos] > 0:
                nums[pos] *= -1
        print(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                solucao.append(i+1)
        print(solucao)
        return solucao

# a = Solution()
# a.findDisappearedNumbers([4,3,2,7,8,2,3,1])