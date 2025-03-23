import re
import string

class RedditTextCleaner:
    """
    RedditTextCleaner is a utility class for cleaning and preprocessing text data,
    specifically designed for Reddit posts or comments. It provides functionality
    to remove mentions, URLs, emojis, hashtags, and special characters, as well as
    normalize whitespace and convert text to lowercase.

    Attributes:
        remove_mentions (bool): Whether to remove mentions (e.g., @username) from the text.
        remove_urls (bool): Whether to remove URLs from the text.
        remove_emojis (bool): Whether to remove emojis from the text.
        remove_hashtags (bool): Whether to remove hashtags (e.g., #topic) from the text.
        lowercase (bool): Whether to convert the text to lowercase.

    Methods:
        clean(text: str) -> str:
            Cleans the input text based on the specified attributes. Removes unwanted
            elements such as URLs, mentions, emojis, hashtags, and special characters,
            normalizes whitespace, and optionally converts the text to lowercase.

            Args:
                text (str): The input text to be cleaned.

            Returns:
                str: The cleaned and preprocessed text. If the input is not a string,
                an empty string is returned.
    """
    def __init__(self, remove_mentions=True, remove_urls=True, remove_emojis=True,
                 remove_hashtags=True, lowercase=True):
        self.remove_mentions = remove_mentions
        self.remove_urls = remove_urls
        self.remove_emojis = remove_emojis
        self.remove_hashtags = remove_hashtags
        self.lowercase = lowercase

        # Precompile regex patterns for performance
        self.url_pattern = re.compile(r'http\S+|www.\S+')
        self.mention_pattern = re.compile(r'@\w+')
        self.hashtag_pattern = re.compile(r'#\w+')
        self.extra_spaces_pattern = re.compile(r'\s+')
        self.emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "]+", flags=re.UNICODE)

    def clean(self, text):
        try:
            if not isinstance(text, str):
                return ""

            # Remove URLs
            if self.remove_urls:
                text = self.url_pattern.sub('', text)

            # Remove mentions
            if self.remove_mentions:
                text = self.mention_pattern.sub('', text)

            # Remove hashtags
            if self.remove_hashtags:
                text = self.hashtag_pattern.sub('', text)

            # Remove emojis
            if self.remove_emojis:
                text = self.emoji_pattern.sub('', text)

            # Remove special characters (keep alphanumerics and spaces)
            text = text.translate(str.maketrans('', '', string.punctuation))

            # Normalize whitespace
            text = self.extra_spaces_pattern.sub(' ', text).strip()

            # Lowercase
            if self.lowercase:
                text = text.lower()

            return text

        except Exception as e:
            print(f"Error cleaning text: {e}")
            return ""

