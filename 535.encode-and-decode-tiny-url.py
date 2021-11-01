#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import random
class Codec:
    def __init__(self):
        self.longShort = {}
        self.shortLong = {}
        self.alphaBeta = "abcdefghijklmnopqrstuvwxyz0123456789"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.longShort:
            suffix = random.sample(self.alphaBeta, 8)
            while "http://tinyurl.com/" + "".join(suffix) in self.shortLong:
                suffix = random.sample(self.alphaBeta, 8)
            tinyUrl = "http://tinyurl.com/" + "".join(suffix)
            self.longShort[longUrl] = tinyUrl
            self.shortLong[tinyUrl] = longUrl
            return tinyUrl
        else:
            return self.longShort[longUrl]
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl not in self.shortLong:
            return None
        return self.shortLong[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

