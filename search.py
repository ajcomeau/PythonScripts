import sys

# Search.py - A generic text file search script.
# Accepts file path/name, search string and optional output file.
# See error message below for examples.

ln = 0              # Line count for output
match = 0           # Match count
errMsg = False      # Error flag
outputFile = None   # Optional output file

if len(sys.argv) < 3:   # Missing arguments
    errMsg = True
elif len(sys.argv) == 4: #Output file specified
    outputFile = sys.argv[3]
    out = open(outputFile, "w")
    
if errMsg == False:
    try:
        # Move through the file looking for matches.
        # Print to screen and output to file if specified.
        for line in open(sys.argv[1]):
            ln += 1
            if sys.argv[2].lower() in line.lower():
                match += 1
                print("Line " + str(ln) + ":")
                print(line)
                if outputFile != None: 
                    out.write("Line " + str(ln) + ":\n")
                    out.write(line+"\n")

        # Count of matches
        print(str(match) + " match(es) found.")
        
    except FileNotFoundError:
        print("Input file, " + sys.argv[1] + " not found.")
        errMsg = True

# Notify user on error
if errMsg:
    print("Please specify the file and the text to search for.")
    print("Example: python search.py file.txt foo")
    print("Example: python search.py file.txt 'foo bar'")

# Cleanup
if outputFile != None:
    out.close()
