# [232. 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/submissions/ "232. 用栈实现队列")
```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.helper:
            return self.helper.pop()
        else:
            while self.stack:
                self.helper.append(self.stack.pop())
            return self.helper.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack:
            return self.stack[0]
        else:
            return self.helper[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.stack or self.helper else True
```
# [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/ "20. 有效的括号")
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif stack and i == d[stack.pop()]:
                continue
            else:
                return False
        return True if not stack else False
```