import sys
import io
# A short script to count the occurrences of each word in a text file
# and list the words in descending order of frequency

wordDict = {}
outputFile = None
outFile = None

if len(sys.argv) == 1:      # Input file
    print("Please specify a file to analyze.")
    sys.exit(0)

if len(sys.argv) > 2:       # Optional output file
    outputFile = sys.argv[2]

try:
    with io.open(sys.argv[1], 'r') as f:
        text = f.read().lower()
    # Remove punctuation
    wordSet = set(text.translate(str.maketrans("-–_;:()[].,!?%\"\'`‘’“”", "                     ", "")).split())

    # Create dictionary of words
    for word in wordSet:
        wordDict[word] = text.count(word)

    # Sort
    wordsByCount = dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))

    # Print and output if specified
    if outputFile is not None:
        outFile = io.open(outputFile, 'w')

    for word, count in wordsByCount.items():
        print(f"{word}: {count}")
        if outputFile is not None:
            outFile.write(f"{word}: {count}\n")

    # Close output file
    if outFile is not None:
        outFile.close()

except FileNotFoundError:
    print("Input file, " + sys.argv[1] + " not found.")
    errMsg = True






