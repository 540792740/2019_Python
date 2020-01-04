'''
Question:
1.  I need to design a word search dictionary.
2.  AddWord(word), search(word), init(),
3.  Input Addword('string') --> return nothing
    search('string') --> return True or False
    search: strin. is equal string, '.' can be any alpha
4.  How about input, input cannot contain '.' right?

Answer:
1.  I should inti a dictionary, using tire to solve
2.  Separate a word into alpha, save into dic, dic at most contain 26 key.
    for each key, contain a 26 key dic.

'''
class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        temp_trie = self.trie
        for c in word:
            if c not in temp_trie:
                temp_trie[c] = {}
            temp_trie = temp_trie[c]
        # Mark word exist
        temp_trie['#'] = '#'

    def search(self, word: str, trie=None) -> bool:
        if trie == None: trie = self.trie
        if not word:
            if '#' in trie: return True
            else: return False
        c = word[0]
        if c == '.':
            for cc in trie:
                if cc != '#' and self.search(word[1:], trie[cc]):
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
