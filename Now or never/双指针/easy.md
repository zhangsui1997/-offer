# [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/ "167. 两数之和 II - 输入有序数组")
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        left = 0
        right = l - 1
        while left != right:
            res = numbers[left]+numbers[right]
            if res>target:
                right-=1
            elif res<target:
                left+=1
            else:
                return [left+1,right+1]
```

# [633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/ "LeetCode633. 平方数之和")
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            res = left*left+right*right
            if res==c:
                return True
            elif res>c:
                right-=1
            else:
                left+=1
        return False
```

# [345. 反转字符串中的元音字母](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/submissions/ "345. 反转字符串中的元音字母")
输入: "leetcode"
输出: "leotcede"
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        res = "aeiouAEIOU"
        s = [i for i in s]
        l, r = 0, len(s)-1
        while l < r:
            if s[l] in res and s[r] in res:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in res:
                    l += 1
                if s[r] not in res:
                    r -= 1
        return "".join(s)
```
# [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/ "680. 验证回文字符串 Ⅱ")
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 因为只删除一个字符串所有可以左右指针
        # 遇到不相等删左或右在判断后面的是否是回文
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1)
            l+=1
            r-=1
        return True

    def isPalindrome(self, s, l, r):
        if l>r:
            return False
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
```
# [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/ "88. 合并两个有序数组")
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p = len(nums1)-1
        p2 = n-1

        while p1>=0 and p2>=0:
            if nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2-=1
            else:
                nums1[p] = nums1[p1]
                p1-=1
            p-=1
        # nums2要是还有剩余就是别nums1中都要小的 直接替换
        nums1[:p2 + 1] = nums2[:p2 + 1]
```