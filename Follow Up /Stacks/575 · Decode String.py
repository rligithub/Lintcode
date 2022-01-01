class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        if not s:
            return
        stack = []
        string = ''
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                stack.append(string)
                string = []
            elif char = ']':
                newstring = string * num
                string = stack.pop() + newstring
                num = 0

            else:  # char.isalpha()
                string += char

        return string
