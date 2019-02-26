# We can import in this way without and alias
# import chapter.modularity.words

# We can import in this way with and alias
# import chapter.modularity.words as w

# We can import also with from and import as follow also with or without alias in this case we alias the function d()
# from chapter.modularity.words import fetch_words as d

# We want a several imports we can have only by separate them by a comma an optionally we can have them in parenthesis

from chapter.modularity.words import (fetch_words, print_items, main)

print_items(fetch_words())

print("----------")

main()
