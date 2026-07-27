from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        while a!=b:
            if a:
                a=a.next
            else:
                a=headB
            if b:
                b=b.next
            else:
                b=headA
        return a

# ============ 测试代码 ============
# 手动构造相交链表
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

# 测试
solution = Solution()
result = solution.getIntersectionNode(headA, headB)
print(f"交点值: {result.val if result else 'None'}")  # 输出: 8