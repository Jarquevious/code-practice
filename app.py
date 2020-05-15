"""Given a string containing a long text, find the most commonly"""
"""occurring word in the text as well as its count."""

from collections import Counter
# word_set = "This is a...."
word_set = " This is a series of strings to count " \
   "many words . They sometime hurt and words sometime inspire "\
   "Also sometime fewer words convey more meaning than a bag of words "\
   "Be careful what you speak or what you write or even what you think of. "\
# Create list of all the words in the string
word_list = word_set.split()            # word_list = word_set.split   output: "This", "is", "a", "series"....

# Get the count of each word.
word_count = Counter(word_list)         # word_count = Counter(word_list) output: word: count, word:count

# Use most_common() method from Counter subclass
print(word_count.most_common(7))        # word_count.most_common(7) = ((word, count), (word, count), (word, count), (word, count), (word, count), (word, count), (word, count))



