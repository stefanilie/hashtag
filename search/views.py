import sys
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import SearchForm
from .models import Search

#TODO: add new page to send results of query to.
#name it, i dunno, results.html
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



	'''if request.method == 'GET':
		form = SearchForm()
		arrTweets=''
	elif request.method == 'POST':
		form = SearchForm(request.POST)
		arrTweets=''
		if form.is_valid():
			if form.is_valid():
				cleaned_data = form.cleaned_data
				strTerm = cleaned_data['search']
				arrTweets = getTweets(strTerm)
				print ("arrtwtter:"+str(arrTweets))
	context = {
		"form": form,
		"tweets": arrTweets
	}
	template = 'search.html'
	return render(request, template, context)'''

#todo: add results to page

#def search(request):
	#add if post or if get and call 
	#getTweets with searchfield content
	# if request.method == 'GET':
	# 	form = SearchForm()

	# elif request.method == 'POST':
	# 	form=

	# form=SearchForm(request.POST or None)
	# context = {"form": form}
	# template="search.html"
	# return render(request, template, context)

#add search field contents
#add options for popular, recent, no. of results, 
def getTweets(strTerm):
	try:
		import twitter
		api=twitter.Api('49tlKU14YrVhPyQTetupdOG1P', 'PyJ0sZuxNlPftq4h06lob8NWCndIud4Ej2WQEEN8rl55HZZNpM', '367335159-VEx8tRMHEfkMQXA92PWtFCHN6ZqxasYoLfYOZj1u', 'TOM1yK1cAKKpX4MvjpPsDkifMbSz6nLQqrXVqYs0WDZj9')
		searchResults=api.GetSearch(term=strTerm,count=10,result_type='popular')
		return searchResults
	except:
		print str(sys.exc_info())
		return "Problem with twitter import."


