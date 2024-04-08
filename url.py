import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Generate a unique hash for the long URL
        hash_object = hashlib.md5(long_url.encode())
        hash_value = hash_object.hexdigest()[:6]

        # Create the short URL using the hash value
        short_url = f"http://short.url/{hash_value}"

        # Store the mapping between the short URL and long URL
        self.url_mapping[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        # Retrieve the long URL from the mapping
        return self.url_mapping.get(short_url, "Short URL not found")

# Example usage
if __name__ == "__main__":
    shortener = URLShortener()
    long_url = input("Enter the long URL: ")
    short_url = shortener.shorten_url(long_url)
    print("Shortened URL:", short_url)

    # Expand a short URL
    short_url_to_expand = input("Enter the short URL to expand: ")
    long_url_expanded = shortener.expand_url(short_url_to_expand)
    print("Expanded URL:", long_url_expanded)
    