class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # According the question, return 0 when there is no endWord
        if endWord not in wordList: return 0

        # Transform input into set, which can be detect easily
        front_word = set([beginWord])
        end_word = set([endWord])
        wordList = set(wordList)
        length = 2

        while front_word:
            # Init temp to save word just one character diff with font
            temp = set()
            for word in front_word:
                for index in range(len(beginWord)):
                    for alpha in 'abcdefghigklmnopqrstuvwxyz':
                        temp.add(word[:index] + alpha + word[index + 1:])
            front_word = temp & wordList
            print(front_word)
            if front_word & end_word:
                return length

            length += 1

            if len(front_word) > len(end_word):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front_word, end_word = end_word, front_word

            # remove transformations from wordDict to avoid cycle
            wordList -= front_word

        return 0


if __name__ == '__main__':
    S = Solution()
    test = S.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(test)
    # a = 'word'
    # b = 'aord'
    # print(a & b)


class Solution1(object):
    def ladderLength1(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList: return 0
        beginWord = set([beginWord])
        endWord = set([endWord])
        visited = beginWord
        ls = 1
        while not beginWord & endWord:
            temp_beginWord = set()
            # Traverse all word in set beginWord
            for word in beginWord:
                print(word)
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        temp = word[:i] + j + word[i + 1:]
                        if  temp in wordList and temp != word:
                            temp_beginWord.add(temp)
            beginWord = temp_beginWord
            if not beginWord: return 0
            ls += 1
            if len(beginWord) > len(endWord):
                # swap front and back for better performance (fewer choices in generating nextSet)
                beginWord, endWord = endWord, beginWord
            wordList -= beginWord
        return ls

if __name__ == '__main__':
    S = Solution1()
    test = S.ladderLength1("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    test = S.ladderLength1("hot", "dog", ["hot","dog"])
    print(test)
    # a = 'word'
    # b = 'aord'
    # print(a & b)

