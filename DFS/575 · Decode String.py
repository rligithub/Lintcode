class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        #base case
        # case 1 --> digit => record and save num = digit in stack
        # case 2 --> letter => add letter to prevStr
        # case 3 --> "[" => reset curStr = ""
        # case 4 --> "]" => pop num from stack, update curStr = prevStr + curStr * num

        stack = []
        curStr = ''
        curNum = 0
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)       #conver to multiple digits if needed
            elif char == "[":
                stack.append(curStr)
                stack.append(curNum)
                curStr = ''
                curNum = 0

            elif char == "]":
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + curStr * num
            else:
                curStr += char

        return curStr

s = "3[a]2[bc]"
a = Solution()
print(a.expressionExpand(s))




