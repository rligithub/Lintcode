class Solution(object): # queue + dfs

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if not nestedList:
            return []
        res = []
        for sublist in nestedList:
            if isinstance(sublist, int):
                res.append(sublist)
            else:
                res.extend(self.flatten(sublist))
        return res