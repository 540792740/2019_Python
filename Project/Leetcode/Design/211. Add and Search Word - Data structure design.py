class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word):
        if trie == None:
            trie = self.trie
        if not word:
            if '#' in trie:
                return True
            else:
                return False
        c = word[0]
        if c =='.':
            for cc in trie:
                if cc != '#' and self.search(word[1 : ], trie[cc]):
                    return True
        elif c in trie:
            return self.search(word[1:], trie[c])
        return False

if __name__ == '__main__':
    S = WordDictionary
    test = S.addWord()
    test = S.addWord()
    test = S.addWord()
    print(test)
