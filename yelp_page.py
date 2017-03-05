from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import pprint as pp 

term = input("search term") 


def yelp_page(term):
# read API keys
	auth = Oauth1Authenticator(
    consumer_key="c1ZyFADSA3mh2WytrZ3HRA",
    consumer_secret="MFFJp33GXsUFjy2mzwZ5uZ_3eKY",
    token="ZrWxEGIMFWpBORaXPjgiBw0qQfQocKby",
    token_secret="1TUAHpk7VGsfyEH1pqGguWg6qms")
	
	client = Client(auth)
	
	location = "Philadelphia, PA"
	params = {

	    'term': term,
	    'lang': 'en',
	    'limit': 3
	}

	response = client.search(location, **params)
	businesses = []
	for business in response.businesses:
	    businesses.append({"name": business.name, 
	    	"website": business.url
	    	  })
	return '<a href="{}">{}</a>'.format(business.url, business.name)
# businesses= get_businesses("Philadelphia", 'career')
# print(businesses)



