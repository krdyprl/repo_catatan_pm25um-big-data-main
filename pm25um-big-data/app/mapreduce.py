words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Map step: turn each word into a key-value pair (word, 1)
mapped = [(word, 1) for word in words]

# Reduce step: sum counts for each unique word
from collections import defaultdict
reduced = defaultdict(int)
for word, count in mapped:
    reduced[word] += count

print(dict(reduced))
# {'apple': 3, 'banana': 2, 'orange': 1}
