class Solution:
    def findLastTwo(self, s):
        # Split string into a list
        string_list = s.split(' ')

        # traverse list and save last two characters into list
        for i in range(len(string_list)):
            string_list[i] = ''.join(string_list[i][-1] + string_list[i][-2])

        # Join list into string and return
        return ' '.join(string_list)


if __name__ == '__main__':
    S = Solution()
    test = S.findLastTwo('apple banana bat liquor times pha alpha')
    print(test)