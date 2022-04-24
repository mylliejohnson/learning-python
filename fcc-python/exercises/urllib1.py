import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # makes socket calls, creates handle
for line in fhand:
    print(line.decode().strip())

# you dont get the headers, just the content