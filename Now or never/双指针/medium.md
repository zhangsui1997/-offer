# [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/ "524. 通过删除字母匹配到字典里最长单词")
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
```python
class Solution:
    def findLongestWord(self, s: str, d) -> str:
        ans = ""
        for word in d:
            l1 = len(ans)
            l2 = len(word)
            if l1 > l2:
                continue
            if self.is_sub(s, word):
                ans = min(ans, word) if l1 == l2 else word
        return ans

    def is_sub(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)
```