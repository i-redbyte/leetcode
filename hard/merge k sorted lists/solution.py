from typing import List, Optional
from utils import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        for i in lists:
            while i:
                tmp.append(i.val)
                i = i.next
        if len(tmp) == 0:
            return
        tmp.sort()
        result = root = ListNode(tmp[0])
        for i in range(1, len(tmp)):
            result.next = ListNode(tmp[i])
            result = result.next
        return root


s = Solution()
l1 = ListNode(1, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, ListNode(6, None))
res = s.mergeKLists([l1, l2, l3])
print("Result:")
result = ""
while res is not None:
    result += "{} ".format(res.val)
    res = res.next
print(result)
