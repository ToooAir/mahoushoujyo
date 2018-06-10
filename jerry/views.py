from django.shortcuts import render_to_response

# Create your views here.
from .models import Restaurant,Food

def index(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('jerry/menu.html',locals())
