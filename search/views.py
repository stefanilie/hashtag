from django.shortcuts import render
from .forms import SearchForm
from .models import Search

def home(request):
	# context= {}
	# template= "home.html"
	# return render(request, template, context)
	form=SearchForm(request.POST or None)
	context = {"form": form}
	template="home.html"
	return render(request, template, context)