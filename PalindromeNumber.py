class Solution:
    def isPalindrome(self, x: int) -> bool:
        strValue = str(x)
        strCopy = strValue[::-1]
        if strValue == strCopy:
            return True
        else:
            return False


solucao = Solution()
print(solucao.isPalindrome(121))
