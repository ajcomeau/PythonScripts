import sys
import requests
import bs4

# HTMLSearch.py - A search script for finding class divs in an HTML file.
# Accepts file path/name and optional output file.
# See error message below for examples.

searchValues = ["_2pin", "_a72d"] # Search strings, can include classes or IDs
ln = 0              # Line count for output
match = 0           # Match count
errMsg = False      # Error flag
outputFile = None   # Optional output file

if len(sys.argv) < 2:   # Missing arguments
    errMsg = True
elif len(sys.argv) == 3: #Output file specified
    outputFile = sys.argv[2]
    out = open(outputFile, "w", encoding='utf-8')
    
if errMsg == False:
    try:
        # Move through the file looking for matches.
        # Print to screen and output to file if specified.
        with open(sys.argv[1], "r", encoding='utf-8') as f:
            htmlsource = f.read()
            pagecontent = bs4.BeautifulSoup(htmlsource, "html.parser")
            for postDiv in pagecontent.find_all("div", class_=searchValues):
                for innerDiv in postDiv:
                    if len(innerDiv.getText()) > 0:
                        print(innerDiv.getText())
                        if outputFile != None: 
                            out.write(innerDiv.getText() + "\n")
        
    except FileNotFoundError:
        print("Input file, " + sys.argv[1] + " not found.")
        errMsg = True

# Notify user on error
if errMsg:
    print("Please specify the file and an optional output file.")
    print("Example: python search.py file.txt")
    print("Example: python search.py file.txt output.txt")

# Cleanup
if outputFile != None:
    out.close()

