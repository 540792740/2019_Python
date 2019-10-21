class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        index = [0 for i in range(10)]
        h = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        res = []
        self.time_helper(index, num, 0, 0,res, h)
        return res

    def time_helper(self, index, n, lit, x, res, h):
        if lit == n:
            hour = 0
            minute = 0
            for i in range(0, 4):
                if index[i] == 1:
                    hour += h[i]
            for j in range(4, 10):
                if index[j] == 1:
                    minute += h[j]
            if minute < 60 and hour < 12:
                if minute < 10:
                    res.append(str(hour % 12) + ':0' + str(minute))
                else:
                    res.append(str(hour % 12) + ':' + str(minute))
            return
        for i in range(x, 10):
            # print(index)
            index[i] = 1
            self.time_helper(index, n, lit + 1, i + 1,res, h)
            index[i] = 0







if __name__ == '__main__':
    S = Solution()
    test = S.readBinaryWatch(2)
    # test = S.readBinaryWatch(10)
    # test = S.readBinaryWatch(0)
    print(test)