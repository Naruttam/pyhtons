#! python3
#lucky.py - opens several google search results

import requests, sys, webbrowser, bs4

print("Googling...") #display text while downloading the google page

res = requests.get("https://www.google.com/search?q="+' '.join(sys.argv[1:]))
res.raise_for_status()

#Retireve top search results links.

soup = bs4.BeautifulSoup(res.text)


#Open a browser tab for each result.

linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #webbrowser.open('http://google.com'+linkElems[i].get('href'))
    print(linkElems[i])
