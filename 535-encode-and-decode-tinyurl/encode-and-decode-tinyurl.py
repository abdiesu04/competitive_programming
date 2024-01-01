# class Codec:
#     def __init__(self):
#         self.encodeMap = {}
#         self.decodeMap = {}
#         self.base = "http://tinyurl.com/"

#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         if longUrl not in self.encodeMap: 
#             shortUrl = self.base + str(len(self.encodeMap) + 1)
#             self.encodeMap[longUrl] = shortUrl
#             self.decodeMap[shortUrl] = longUrl
#         return self.encodeMap[longUrl]

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.decodeMap[shortUrl]
import random

class Codec:

    res = {}
    chars = 'abcdefghijklmnopqrstuvwxvz'
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = "http://tinyurl.com/" + ''.join(random.choice(self.chars) for _ in range(5))

        self.res[url] = longUrl

        return url
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.res[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))