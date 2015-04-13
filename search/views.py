import sys
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import SearchForm
from .models import Search

def home(request):
	if request.POST:
		arrTweets = getTweets(request.POST['search'])
		print arrTweets
		context = {
			'tweets': arrTweets,
			'form' : SearchForm()
		}
		return render(request, 'search.html', context)
	else:
		context = {
			'form': SearchForm()
		}
		return render(request, 'search.html', context)

#add options for popular, recent, no. of results, 
def getTweetsID(strTerm):
	arrToReturn=[]
	try:
		import twitter
		api=twitter.Api('49tlKU14YrVhPyQTetupdOG1P', 'PyJ0sZuxNlPftq4h06lob8NWCndIud4Ej2WQEEN8rl55HZZNpM', '367335159-VEx8tRMHEfkMQXA92PWtFCHN6ZqxasYoLfYOZj1u', 'TOM1yK1cAKKpX4MvjpPsDkifMbSz6nLQqrXVqYs0WDZj9')
		searchResults=api.GetSearch(term=strTerm, count=5, result_type="popular")
		for result in searchResults:
			arrToReturn.append(result.id)
		return arrToReturn
	except:
		print str(sys.exc_info())
		return "Problem with twitter import."


#todo: get tweets by above function and use id to embed
def getTweets(strTerm):
	arrResults = getTweetsID(strTerm)
	arrToReturn = []
	try:
		from embed.utils import Embed
		Embed.consumer_key = '49tlKU14YrVhPyQTetupdOG1P'
		Embed.consumer_secret = 'PyJ0sZuxNlPftq4h06lob8NWCndIud4Ej2WQEEN8rl55HZZNpM'
		Embed.oauth_token = '367335159-VEx8tRMHEfkMQXA92PWtFCHN6ZqxasYoLfYOZj1u'
		Embed.oauth_token_secret = 'TOM1yK1cAKKpX4MvjpPsDkifMbSz6nLQqrXVqYs0WDZj9'

		Embed.config = {
  			  'height': '300',
 			   'width': '400',
		}
		for result in arrResults:
			embed_code = Embed.get_twitter_embed_by_id(id=result)
			arrToReturn.append(embed_code)

		return arrToReturn
	except:
		print str(sys.exc_info())
		return "Problem with twitter import."


'''
	TODO: 
	-add model for facebook posts
	- see how we can make request to facebook
	- get and parse response from sed request
	- put content into serch page
	- make search-page friendly-er
'''