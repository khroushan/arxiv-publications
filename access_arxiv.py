# To read, parse and analyze scientific publication using Arxiv api,
# for arXiv documentation, look at:
# http://export.arxiv.org/api_help/docs/user-manual.html

# author: Amin Ahmadi
# date: April 2020
########## 
import urllib.request
import time
import feedparser

# '<?xmlversion="1.0" encoding="UTF-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n
base_url = "http://export.arxiv.org/api/query?"

# search parameters
search_query = 'all:covid-19'   # search for covid-19 in all fields
start = 0                       # start at the first result
total_results = 2               # wants 20 total results
results_per_iteration = 2       # 5 results at a time
wait_time = 3                   # number of seconds to wait between calls

print("Searching arXiv for {}".format(search_query))

for i in range(start, total_results, results_per_iteration):

    print("Results {} - {}".format(i, i+results_per_iteration))

    query = "search_query={}&start={}&max_results={}".format(search_query,
                                                             i,
                                                             results_per_iteration)
    # perform a GET request using the base url and query
    request = urllib.request.urlopen(base_url+query)
    response = request.read()

    # parse the response using feedparser
    feed = feedparser.parse(response)


    # Run through each entry, and print out information
    for entry in feed.entries:
        print(entry.keys())
        print("arXiv-id: {}".format(entry.id.split('/abs/')[-1]))
        print("Title: {} \n".format(entry.title))
        print("update date: {}".format(entry.updated))
        print("Summary:\n {}\n".format(entry.summary))

    print("wait for {} seconds".format(wait_time))
    time.sleep(wait_time)
