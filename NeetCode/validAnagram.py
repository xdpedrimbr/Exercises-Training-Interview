class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slower = s.lower()
        tlower = t.lower()

        print(slower)
        print(tlower)

        copy1 = list(slower)
        copy2 = list(tlower)

        copy1.sort()
        copy2.sort()


        if (copy1) == (copy2):
            return True
        else:
            return False
        
        

solucao = Solution()
print(solucao.isAnagram("Pedro", "Edpro"))