import urllib2
import urllib
import json

outfile = open('pagedump.txt', 'w')
def get_wiki_pages(user, continueString=""): #fetches json documenting revisions from the wikipedia api
	#loooong string containing the basic form for the query we want for the 		wikipedia API
	wiki_api_string = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucprop=title&ucnamespace=0&uclimit=max&format=json'	
	response = urllib2.urlopen(wiki_api_string + '&ucuser=' + user + continueString) #Opens a 		connection to the Wikipedia API
	wiki_raw = response.read() #Reads the data from the connection
	wiki_json = json.loads(wiki_raw) #Loads the data into json format
	return wiki_json

def get_wiki_categories(titles, continueString=""): #fetches json documenting revisions from the wikipedia api
	#loooong string containing the basic form for the query we want for the 		wikipedia API
	wiki_api_string = 'http://en.wikipedia.org/w/api.php?action=query&prop=categories&cllimit=max&format=json'	
	response = urllib2.urlopen(wiki_api_string + '&titles=' + titles + continueString) #Opens a 		connection to the Wikipedia API
	wiki_raw = response.read() #Reads the data from the connection
	wiki_json = json.loads(wiki_raw) #Loads the data into json format
	return wiki_json

result = get_wiki_pages('mav')
title_list = []

while 'query-continue' in result:
	for contrib in result['query']['usercontribs']:
		if contrib['title'] not in title_list:
			title_list.append(contrib['title'])
	uccontinue = "&uccontinue=" + result['query-continue']['usercontribs']['uccontinue']
	result = get_wiki_pages('mav', uccontinue)

for contrib in result['query']['usercontribs']:
		if contrib['title'] not in title_list:
			title_list.append(contrib['title'])
title_string = ""
for title in title_list:
	title_string = title_string + title.encode('utf-8') + "|"

title_url = urllib.quote(title_string, safe="|")
outfile.write(title_url)

