class Solution:
    def mostCommon(self, paragraph, banned):
        dic = {}
        for c in '!?,;.':
            paragraph = paragraph.replace(c, ' ')
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
        print(dic.get)
        return max(dic, key = dic.get)

if __name__ == '__main__':
    S = Solution()
    test = S.mostCommon("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(test)