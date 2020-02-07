# [19. 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/ "LeetCode19. 删除链表的倒数第N个节点")
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
		# 让快指针先走n+1步数再一起走
		# 此时fast到底时候 slow指向要删除节点的前一个节点
        n += 1
        while n>0:
            if not fast:
			# 题意保证了n的有效性
			# 如果删除的n是链表的长度就是删除头节点会越界
                return head.next
            fast = fast.next
            n-=1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
```

# [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/ "24. 两两交换链表中的节点")
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head

        pre_head = pre # 要一个互换两节点的前一个节点
        while pre_head.next and pre_head.next.next:
            first, second = pre_head.next, pre_head.next.next
			# 前一个和后一个互换
            first.next = second.next
            second.next = first

			# 互换前的pre_head指向的是first
			# 互换后second在前了要指向second
            pre_head.next = second
			# 再让pre_head指向互换后的first继续往下走
            pre_head = first

        return pre.next
```
# [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/ "445. 两数相加 II")
### 不使用int() str()等内置函数的解法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = self.get_stack(l1)
        stack2 = self.get_stack(l2)
        res = []
        pre = 0 # 大于10要进一位
        while stack1 and stack2:
            num = stack1.pop()+stack2.pop()+pre
            if num>9:
                pre = 1
                num -= 10
            else:
                pre = 0
            res.append(num)

        others = stack1 if stack1 else stack2
        while others:
            num = others.pop()+pre
            if num>9:
                pre = 1
                num -= 10
            else:
                pre = 0
            res.append(num)

		# 要考虑可能最后pre=1的情况
        pre_node = ListNode(pre) if pre==1 else None
		# 头节点的前驱节点
        pre_head = ListNode(None)

        cur = pre_head
        cur.next = pre_node if pre_node else None
        cur = cur.next if cur.next else cur

        for i in res[::-1]:
            node = ListNode(i)
            cur.next = node
            cur = node
        return pre_head.next

    def get_stack(self,node):
        stack = []
        while node:
            stack.append(node.val)
            node=node.next
        return stack
```
# [234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/ "234. 回文链表")
O(1)空间复杂度解决
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
		# 快慢指针 如果quick到底则slow到中间或中间前一位置
        quick, slow = head, head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next

        # 翻转后面的链表
		# 1->2->3->4 变成 1->2<-3<-4
        pre = self.reverse_list(slow)

        # 首位开始对比
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True

    def reverse_list(self, head):
        cur = head
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
```
# [725. 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts/ "725. 分隔链表")
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if k == 1:
            return [root]

        res = []
        count = 0
        head = root
        while head:
            count += 1
            head = head.next

        length = count // k if count >k else 1
        bigger = count % k if count > k else 0

        for i in range(k):
            pre_head = ListNode(None)
            pre = pre_head
            for j in range(length):
                if root:
                    cur = ListNode(root.val)
                    pre.next = cur
                    pre = cur
                    root = root.next
            if bigger > 0 and root:
                bigger -= 1
                cur = ListNode(root.val)
                pre.next = cur
                root = root.next
            if pre_head.next:
                res.append(pre_head.next)
            else:
                res.append(None)
        return res
```

# [328. 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/solution/ "328. 奇偶链表")
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head
```