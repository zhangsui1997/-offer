将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```
L   C   I   R  
E T O E S I I G  
E   D   H   N  
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
```
L     D     R  
E   O E   I I  
E C   I H   N  
T     S     G  
```


*找规律 写逻辑 考虑边界和循环条件*  


*Z字形状 是一个个 |/| 可以分析出来是|/的一次次循环*  

```
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = [[] for i in range(numRows)]
        foo = 0
        end = len(s)
        while foo<end:
            for i in range(numRows):
                if foo<end:
                    res[i].append(s[foo])
                    foo+=1
            for i in range(numRows-2,0,-1):
                if foo<end:
                    res[i].append(s[foo])
                    foo+=1
        str=""
        for i in range(numRows):
            str+="".join(res[i])
        return str
    ```
