#! Shebang se usa para indicar que interprete deberia de usarse para ejecutar el programa ej  /usr/bin/env python3

"""Retieve and print words form a URL

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


# Two spaces between the functions are part of the python zen sparse is better than dense
# with "with" will manage the resources in order to avoid leaks, is similar to try with resources in java
def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 text document

    Returns:
        A list of string containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for word in items:
        print(word)


def main(url):
    """Print each word from a text document from a URL.
    Args:
        url: The URL of a UTF-8 text
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main()
