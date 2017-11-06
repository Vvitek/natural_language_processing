from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

fdist = FreqDist()
for word in word_tokenize(open('pantadeusz.txt', 'r').read().strip(',.')):
    fdist[word.lower()] += 1

print(fdist.most_common(50))
