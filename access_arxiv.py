# To read, parse and analyze scientific publication using Arxiv api,
# for arXiv documentation, look at:
# http://export.arxiv.org/api_help/docs/user-manual.html

# author: Amin Ahmadi
# date: April 2020
########## 
import urllib.request
import time
import feedparser
import pandas as pd

# '<?xmlversion="1.0" encoding="UTF-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n
base_url = "http://export.arxiv.org/api/query?"

# search parameters
search_query = 'all:covid'   # search for covid-19 in all fields
start = 0                       # start at the first result
total_results = 900             # wants N total results
results_per_iteration = 900     # 5 results at a time
wait_time = 3                   # number of seconds to wait between calls

def get_publication(search_query: str, start:int = 0, total_results:int = 10, results_per_iteration:int = 10):

    print("Searching arXiv for {}".format(search_query))
    for i in range(start, total_results, results_per_iteration):
        print("Results {} - {}".format(i, i+results_per_iteration))

        query = "search_query={}&start={}&max_results={}&sortBy=lastUpdatedDate".format(search_query,
                                                                                    i,
                                                                                    results_per_iteration)
        # perform a GET request using the base url and query
        request = urllib.request.urlopen(base_url+query)
        response = request.read()

        # parse the response using feedparser
        feed = feedparser.parse(response)
        
        counter = 0
        ids = []
        titles = []
        dates = []
        summaries = []
        
        # Run through each entry, and store in lists
        for entry in feed.entries:
            counter += 1
            # print(counter)
            # print("\narXiv-id: {}".format(entry.id.split('/abs/')[-1]))
            # print("Title: {}".format(entry.title))
            # print("Publish date: {}\n".format(entry.published))
            # print("Summary:\n {}\n".format(entry.summary))
            ids.append("{}".format(entry.id.split('/abs/')[-1]))
            titles.append("{}".format(entry.title))
            dates.append("{}".format(entry.published))
            summaries.append("{}".format(entry.summary))

    # print("wait for {} seconds".format(wait_time))
    print("\n==========\n")
    print(counter, len(ids), len(titles), len(dates), len(summaries))
    data_dict = {'id': ids, 'title':titles, 'date':dates, 'summary':summaries}
    data = pd.DataFrame(data=data_dict)

    return data
# print(data.head(3))
# print(data.describe())
data = get_publication(search_query, start, total_results, results_per_iteration)
data.to_csv("covid_publication.csv")
