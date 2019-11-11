class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        current_node = self.root
        val = ""

        for w in word:
            val += w
            if w not in current_node.children:
                current_node.children[w] = TrieNode(val)

            current_node = current_node.children[w]

        current_node.is_word = True

    def search_words_with_prefix(self, prefix):
        current_node = self.root

        for p in prefix:  # O(k)
            if p not in current_node.children:
                return []

            current_node = current_node.children[p]

        words = self.get_words(current_node)  # O(n.l)
        words.sort()  # O(n.logn)

        return words if len(words) <= 3 else words[0:3]

    def get_words(self, node):
        stack = [node]
        res = []

        while stack:
            current_node = stack.pop()

            if current_node.is_word:
                res.append(current_node.val)

            for child in current_node.children.values():
                stack.append(child)

        return res

    # Assume length of query and average length of product name is trivial.
    # Then T(n) = n^2 * logn
    def product_suggestions(self, products, query):
        if len(query) <= 1 or not products:
            return None

        for product in products:  # O(n). n is number of products
            self.insert(product)  # O(l). l is average length of a product name

        custom_queries = []

        for i in range(2, len(query) + 1):  # O(k). k is length of query
            custom_queries.append(query[0:i])

        res = []

        for custom_query in custom_queries:  # O(k)
            res.append(self.search_words_with_prefix(custom_query))  # O(k + n.l + n.logn)

        return res


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False

trie = Trie()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
query = "mouse"
expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")

trie = Trie()
products = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
                    "standing table", "house", "true love", "tracking device"]
query = "ps4"
expected = [["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
query = "tru"
expected = [["tracking device", "true love"], ["true love"]]
self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
query = "t"
self.assertEqual(None, trie.product_suggestions(products, query),
                         "Should return None if query is less than 2 characters")