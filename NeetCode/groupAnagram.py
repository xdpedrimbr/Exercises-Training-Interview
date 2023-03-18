class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        list2 = []
        print(strs)
        for i in strs:
            list1 = list(i)
            list1.sort()
            list2.append(list1)
        
        list3 = []

        for i in range(len(list2)):
            for j in range(1, len(list2)):
                if(list2[i] == list2[j]):
                    list3.append([list2])

        print(list3)
        

solucao = Solution()
print(solucao.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))