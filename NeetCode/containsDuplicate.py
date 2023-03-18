class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for c in range(1, len(nums)):
            if(nums[c] == nums[c - 1]):
                return True
            
        return False

            


            

solucao = Solution()
print(solucao.containsDuplicate([5,2,3,4]))