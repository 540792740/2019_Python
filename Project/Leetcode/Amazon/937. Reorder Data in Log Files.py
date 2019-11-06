'''
Two list, one Save Alpha_log, one save numeral_log
'''

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        Alpha_log = []
        num_log = []
        for log in logs:
            log_split = log.split(" ")
            if log_split[1].isalpha():
                Alpha_log.append((" ".join(log_split[1:]), log_split[0]))
            else:
                num_log.append(log)
            Alpha_log.sort()
            # print(Alpha_log)
        return [letter[1] + " " + letter[0] for letter in Alpha_log] + num_log

if __name__ == '__main__':
    S = Solution()
    test = S.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    print(test)