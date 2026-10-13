#Write a program to count the occurrences of a specific word in a file using regular expressions.

import re

word = input("Enter the word to search: ")

f = open("sample.txt", "r")
text = f.read()
f.close()

count = len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))

print("Occurrences of", word, ":", count)

#Write a program to extract all hyperlinks (<a href="...">) from an HTML file.

import re

f = open("sample.html", "r")
html = f.read()
f.close()

links = re.findall(r'<a\s+[^>]*href=["\'](.*?)["\']', html)

print("Hyperlinks in the HTML file:")

for link in links:
    print(link)

#Sample Html File
"""<html>
<body>
<a href="https://www.google.com">Google</a>
<a href="https://www.python.org">Python</a>
<a href="https://www.wikipedia.org">Wikipedia</a>
</body>
</html>"""


