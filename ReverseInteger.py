class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = x < 0
        x = -x if flag else x
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        res = -res if flag else res
        max_val = (1 << 31) - 1
        # ran = (-max_val - 1, max_val)
        return res if -max_val - 1 <= res <= max_val else 0
