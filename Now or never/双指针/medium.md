# [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/ "524. 通过删除字母匹配到字典里最长单词")
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