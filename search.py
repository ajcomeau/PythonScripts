import sys

# Search.py - A generic text file search script.
# Accepts file path/name and search string.  See error message
# below for examples.

ln = 0
match = 0
errMsg = False

if len(sys.argv) > 2:
    try:
        for line in open(sys.argv[1]):
            ln += 1
            if sys.argv[2].lower() in line.lower():
                match += 1
                print("Line " + str(ln) + ":")
                print(line)

        print(str(match) + " match(es) found.")
        
    except FileNotFoundError:
        print(sys.argv[1] + " not found.")
        errMsg = True

else:
    errMsg = True

if errMsg:
    print("Please specify the file and the text to search for.")
    print("Example: python search.py file.txt foo")
    print("Example: python search.py file.txt 'foo bar'")
