from urllib.request import urlopen

# with "with" will manage the resources in order to avoid leaks, is similar to try with resources in java
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
# Resultara en bytes, cada elemento sera precedido por b'
print(story_words)
# If we want to decode the byte as string we do the following
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

print(story_words)
