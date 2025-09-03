import sys
import io
# A short script to count the occurences of each word in a text file
# and list the words in descending order of frequency

wordDict = {}

if len(sys.argv) > 1:
    with io.open(sys.argv[1], 'r') as f:
        text = f.read().lower()

    wordSet = set(text.translate(str.maketrans("", "", ".,\"")).split())
    for word in wordSet:
        wordDict[word] = text.count(word)

    wordsByCount = dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))

    for word, count in wordsByCount.items():
        print(f"{word}: {count}")


