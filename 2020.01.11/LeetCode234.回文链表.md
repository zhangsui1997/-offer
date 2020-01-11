# [LeetCode234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/ "LeetCode234. 回文链表")
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false

示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

## 常用解法
#### 1.遍历一遍，将值保存到一个栈中。再遍历一遍和栈的出栈顺序对比。
O(n) 时间复杂度和 O(n) 空间复杂度
#### 2.快慢指针，快的一次走两步。当快指针走到头慢指针在中点位置，开始将慢指针后面的值入栈。再遍历和栈的出栈顺序对比。
O(n) 时间复杂度和 O(n) 空间复杂度，但是比1解法稍微快一点。

## 进阶解法
O(n) 时间复杂度和 O(1) 空间复杂度，链表问题的时间复杂度通常都为O(n)。
#### 1.快慢指针，慢指针到中点时将后面的链表逆序。
如 1->2->3->2->1，改成 1->2->3<-2<-1, 要注意偶数项时中点位置。
#### 2.首尾指针，开始对比。
#### 3.记录中点位置，对比完成后，将链表改回去。
```
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        quick, slow = head, head

        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
        mid = slow  # 记录下中点位置 方便后面在逆序回原链表

        # 翻转后面的链表
        pre = self.reverse_list(slow)
        end = pre
        
        # 首位开始对比
        while pre and head:
            if pre.val != head.val:
                # 反转回原样
                self.reverse_list(end)
                return False
            pre = pre.next
            head = head.next
        # 反转回原样
        self.reverse_list(end)
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
