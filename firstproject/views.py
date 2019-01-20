from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')


def count(request):
	data= request.GET['fulltext']
	word_list = data.split()
	list_length = len(word_list)
	worddictinory = {}
	for word in word_list:
		if word in worddictinory:
			worddictinory[word] += 1
		else:
			worddictinory[word] = 1
	sorted_list= sorted(worddictinory.items(), key= operator.itemgetter(1), reverse=True)
	return render(request,'count.html', {'fulltext': data, 'length':list_length, 'worddictinory':sorted_list})
