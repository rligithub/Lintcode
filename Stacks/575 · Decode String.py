class Solution:
    # stack --> only save pre string and number
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        if not s:
            return ''
        stack = []
        string = ''
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                stack.append(string)  # save prev string
                stack.append(num)  # save repeat times
                string = ''
                num = 0
            elif char == ']':
                newnum = stack.pop()
                prevstring = stack.pop()
                string = prevstring + string * newnum

            else:  # char.isalpha()
                string += char

        return string


s = '3[2[ad]3[pf]]xyz'
a = Solution()
print(a.expressionExpand(s))
