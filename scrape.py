import urllib2
import urllib
import json

outfile = open('namedump.txt', 'w')
def get_wiki_users(title, continueString=""): #fetches json documenting revisions from the wikipedia api
	#loooong string containing the basic form for the query we want for the 		wikipedia API
	wiki_api_string = 'http://en.wikipedia.org/w/api.php?action=query&prop=contributors&rvlimit=max&format=json&pcexcludegroup=bot'	
	response = urllib2.urlopen(wiki_api_string + '&titles=' + title + continueString) #Opens a 		connection to the Wikipedia API
	wiki_raw = response.read() #Reads the data from the connection
	wiki_json = json.loads(wiki_raw) #Loads the data into json format
	return wiki_json

results = get_wiki_users("Gilligan\'s_Island")

while 'query-continue' in results:
	for user in results['query']['pages']['87639']['contributors']:
		outfile.write(user['name'] + '\n')	
	pccontinue = "&pccontinue=" + results["query-continue"]["contributors"]["pccontinue"]
        results = get_wiki_users("Gilligan\'s_Island", pccontinue)

