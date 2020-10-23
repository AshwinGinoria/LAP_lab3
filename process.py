import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

## function to find most common least common occuring word
## return counts of all noun words
## plot its histogram
def CountWords(text):
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    tokens = word_tokenize(text)
    
    tokens = [w for w in tokens if w.isalpha()]
    tagged = nltk.pos_tag(tokens)
    filtered = [
        w[0]
        for w in tagged
        if w[1] == "NN" or w[1] == "NNP" or w == "NNS" or w == "NNPS"
    ]
    
    counts = Counter(filtered)
    return counts

def PlotWordHistogram(text):
    counts = CountWords(text)

    labels, values = zip(*counts.items())

    indSort = np.argsort(values)[::-1]
    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]
    indexes = np.arange(len(labels))

    bar_width = 0.35

    plt.bar(indexes, values)
    plt.xticks(indexes + bar_width, labels, rotation=90)

    return plt
