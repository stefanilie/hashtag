from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import SearchForm
from .models import Search

def search(request):
	#add if post or if get and call 
	#getTweets with searchfield content
	form=SearchForm(request.POST or None)
	context = {"form": form}
	template="search.html"
	return render(request, template, context)

def home(request):
	context={'homepage': homepage, 'tweets': getTweets()}
	return render_to_response('home.html', context, context_instance=RequestContext(request))

#add search field contents
#add options for popular, recent, no. of results, 
def getTweets(strTerm):
	try:
		import twitter
		api=twitter.Api()
		searchResults=api.GetSearch(strTerm, None, None, None, None, 10, None, None,  "popular", True)
		return searchResults
	except:
		return "Problem with twitter import."


