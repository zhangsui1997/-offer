# [LeetCode138. 复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/138-fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-ha-xi-/)
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

    val：一个表示 Node.val 的整数。
    random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

## 常用解法
O(n) 时间复杂度和 O(n) 空间复杂度
```python
# 利用哈希结构深复制
class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        res = {}
        cur = head
        while cur:
            res[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            res[cur].next = res[cur.next] if cur.next else Node
            res[cur].random = res[cur.random] if cur.random else Node
            cur = cur.next
        return res[head] if res else None
```
## 进阶解法
O(n) 时间复杂度和 O(1) 空间复杂度
```python
class Solution2:
        def copyRandomList(self, head: 'Node') -> 'Node':
            if not head:
                return head
            # 遍历并拷贝每一个节点，将拷贝节点放在原来节点的旁边，创造出一个旧节点和新节点交错的链表。
            cur = head
            while cur:
                clone_node = Node(cur.val)
                clone_node.next = cur.next
                cur.next = clone_node
                cur = clone_node.next

            # 遍历并用旧节点的 random 指针去更新对应新节点的 random 指针。
            cur = head
            while cur:
                cur.next.random = cur.random.next if cur.random else None
                cur = cur.next.next

            # next 指针也需要被正确赋值 遍历以便将新的节点正确链接同时将旧节点重新正确链接。
            cur = head
            clone_head = head.next
            clone_cur = head.next
            while cur:
                cur.next = cur.next.next if cur.next else None
                clone_cur.next = clone_cur.next.next if clone_cur.next else None
                clone_cur = clone_cur.next
                cur = cur.next
            return clone_head
```
