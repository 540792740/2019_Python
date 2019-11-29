def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # split all word into set{}
    S = set(words)
    ans = []

    # Traverse all word
    for word in words:
        if not word: continue
        stack = [0]
        used_word = {0}
        ls = len(word)
        while stack:
            node = stack.pop()
            # when single word can combine into word, add into ans.
            if node == ls:
                ans.append(word)
                break
            for j in range(ls - node + 1):
                if (word[node:node + j] in S and # word[node: node + j] in S
                    node + j not in seen and    #Avoid use same element
                    (node > 0 or node + j != ls)):  #node > 0, node + j != ls can prove that the word must be combined.
                    stack.append(node + j)
                    used_word.add(node + j)
                print(seen, word, j, stack)

    return ans
findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])

def findAllConcatenatedWordsInADict1(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    def dfs(word, initial, memo):
        if word in memo:
            return memo[word]
        if word in wordDict and not initial:
            memo[word] = 1
            return True
        for i in range(1, len(word)):
            if word[:i] in wordDict and dfs(word[i:], False, memo):
                memo[word] = 1
                return True
        memo[word] = 0
        return False

    wordDict = set(words)
    ans = []
    for word in words:
        if dfs(word, True, {}):
            ans.append(word)
    return ans