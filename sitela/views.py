from django.shortcuts import render_to_response
from django.http import HttpResponse

# def index(request):
# 	return HttpResponse("WTF")

def search_form(request):
	return render_to_response('sitela/search_form.html')

def search(request):
	request.encoding = 'utf-8'
	message = '我是'+ request.GET['q'] +'艦長我拯救世界。'
	return HttpResponse(message)

# Create your views here.
