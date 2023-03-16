from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1[::-1]
        list2 = l2[::-1]
        aux = ""
        aux2 = ""
        for c in list1:
            aux += str(c)
        for c in list2:
            aux2 += str(c)
        
        num1 = int(aux)
        num2 = int(aux2)
        soma = num1 + num2

        somaStr = str(soma)
        resultado = list(somaStr)

        aux3 = ""

        for c in range(len(resultado)):
            resultado[c] = int(resultado[c])

        final = resultado[::-1]
        return final


solucao = Solution()
solucao.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])
