print('8 · Rotate String')

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        if not s:
            return None
        length=len(s)
        if offset > length:
            offset= offset % length
        self.reverse(s, 0, length - offset - 1)
        self.reverse(s, length - offset, length - 1)
        self.reverse(s, 0, length - 1)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right]= s[right], s[left]
            left +=1
            right -=1




