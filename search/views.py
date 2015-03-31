from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import SearchForm
from .models import Search

#TODO: add new page to send results of query to.
#name it, i dunno, results.html
def home(request):
	form=SearchForm(request.POST or None)
	context = {"form": form}
	template="search.html"
	return render(request, template, context)


def search(request):
	#add if post or if get and call 
	#getTweets with searchfield content
	if request.method == 'GET':
		form = SearchForm()
	elif request.method == 'POST':
		form = SearchForm(request.POST)
		arrTweets=''
		if form.is_valid():
			if form.is_valid():
				cleaned_data = form.cleaned_data
				strTerm = cleaned_data['search']
				arrTweets = getTweets(strTerm)
		context = {
			"form": form,
			"tweets": arrTweets
		}
		template = "search.html"
		return render(request, template, context)

	# form=SearchForm(request.POST or None)
	# context = {"form": form}
	# template="search.html"
	# return render(request, template, context)

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


