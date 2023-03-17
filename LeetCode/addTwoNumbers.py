#ESTA DANDO ERRO

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        resultado = ListNode(0)
        pointer = resultado #todas as vezes que mexermos o pointer, o resutlado mudara

        while l1 or l2 or carry:
            n1 = l1.val if l1.val else 0
            n2 = l2.val if l2.val else 0

            soma = n1 + n2 + carry
            num = soma % 10
            carry = soma // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return resultado.next



input_list1 = [1, 2, 3]
input_list2 = [3, 2, 1]

nodes1 = [ListNode(val = i) for i in input_list1]
for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]

nodes2 = [ListNode(val = i) for i in input_list2]
for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]

solucao = Solution()
print(solucao.addTwoNumbers(nodes1[0], nodes2[0]))




        # A SOLUCAO ABAIXO NAO FUNCIONA, POIS ESTOU TRATANDO A LISTA COMO UM ARRAY
        # list1 = l1[::-1]
        # list2 = l2[::-1]
        # aux = ""
        # aux2 = ""
        # for c in list1:
        #     aux += str(c)
        # for c in list2:
        #     aux2 += str(c)
        
        # num1 = int(aux)
        # num2 = int(aux2)
        # soma = num1 + num2

        # somaStr = str(soma)
        # resultado = list(somaStr)

        # aux3 = ""

        # for c in range(len(resultado)):
        #     resultado[c] = int(resultado[c])

        # final = resultado[::-1]
        # return final