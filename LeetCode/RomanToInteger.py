roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 

class Solution:
    def romanToInt(self, s: str) -> int:
        somaTotal = 0
        for c in range(len(s) - 1, -1, -1): #vai de tras pra frente
            num = roman[s[c]]
            if 3 * num < somaTotal:
                somaTotal = somaTotal - num
            else:
                somaTotal = somaTotal + num
        return somaTotal

solucao = Solution()
print(solucao.romanToInt("IV"))


