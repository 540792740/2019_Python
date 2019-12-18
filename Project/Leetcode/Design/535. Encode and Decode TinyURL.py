class Codec:
    def __init__(self):
        self.dic = {}
        self.key = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        text = 'tinyurl.com' + str(self.key)
        self.dic[text] = longUrl
        self.key += 1
        return text

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))