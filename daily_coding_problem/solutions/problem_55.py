# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.

# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

# Hint: What if we enter the same URL twice?

import hashlib

class url_shortener:

    def __init__(self):
        self.url_map = dict()
        self.hash = hashlib.sha256
        self.prefix = "http://urlshorten.er/"

    def shorten(self, url):
        sha_signature = self.hash(url.encode()).hexdigest()
        short_hash = sha_signature[:6]
        self.url_map[short_hash] = url
        return self.prefix + short_hash

    def restore(self, shortened_url):
        short_hash = shortened_url.replace(self.prefix, "")
        original_url = self.url_map[short_hash]
        return original_url


url = "https://kulsuri.com/portfolio-optimisation/"
us = url_shortener()

short_0 = us.shorten(url)
long_0 = us.restore(short_0)

print(short_0)
print(long_0)

assert us.restore(short_0) == url