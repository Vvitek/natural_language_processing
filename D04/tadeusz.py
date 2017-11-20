from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from re import sub

fdist = FreqDist()
for word in word_tokenize(sub('[^\w\s]','', open('pantadeusz.txt', 'r').read())):
    fdist[word.lower()] += 1

print(fdist.most_common(50))
