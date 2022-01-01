class Solution: # return sorted string by case, use two pointers with opposite directions
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        if len(chars) == 0:
            return True
        left, right = 0, len(chars) -1
        while left <= right:
            if chars[left].islower():
                left += 1
                continue
            if chars[right].isupper():
                right -= 1
                continue
            if chars[left].isupper() and chars[right].islower():
                left += 1
                right -= 1
        return chars