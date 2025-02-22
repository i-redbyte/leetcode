from utils import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            result = (result << 1) | head.next.val
            head = head.next
        return result

    def getDecimalValue2(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            result = result * 2 + head.next.val
            head = head.next
        return result

    def getDecimalValue1(self, head: ListNode) -> int:
        binaries = []
        while head:
            binaries.append(head.val)
            head = head.next
        n = len(binaries) - 1
        result = 0
        p = 0
        for i in range(n, -1, -1):
            result += pow(2, p) * binaries[i]
            p += 1
        return result


s = Solution()
print(s.getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))
print(s.getDecimalValue(ListNode(1, ListNode(1, ListNode(1)))))
# 100100111000 000
print(s.getDecimalValue(
    ListNode(1, ListNode(0, ListNode(0,
                                     ListNode(1, ListNode(0, ListNode(0,
                                                                      ListNode(1, ListNode(1, ListNode(1,
                                                                                                       ListNode(0,
                                                                                                                ListNode(
                                                                                                                    0,
                                                                                                                    ListNode(
                                                                                                                        0,
                                                                                                                        ListNode(
                                                                                                                            0,
                                                                                                                            ListNode(
                                                                                                                                0,
                                                                                                                                ListNode(
                                                                                                                                    0)))
                                                                                                                    )))
                                                                                                       )))))))))))
