#take each line from searches.txt and search the respective text
from googlesearch import search

with open('searches.txt', 'r') as searches:
    for query in searches:
        print(query + ": ")
        for result in search(query, tld="co.in", num=10, stop=10, pause=1):
            print(result)
        print("--------------------------------------")
        