class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    pass
                elif nums[i] + nums[j] == target:
                    return [i, j]

solucao = Solution()
print(solucao.twoSum([1, 2, 3, 4, 5], 9))
