class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        a, b = edges[0]
        c, d = edges[1]

        # node chung giữa 2 cạnh đầu
        if a == c or a == d:
            return a

        return b
        