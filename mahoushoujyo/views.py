from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login	,logout
from django.contrib.auth.models import User 
# import msvcrt
# Create your views here.
def index(request):
	return render(request,'index.html')
def signin(request):
	if request.method == 'POST':
		account = request.POST.get('account')
		password = request.POST.get('password')
		user = authenticate(username=account, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			return redirect('signin') #question
	return render(request,'signin.html')
def register(request):
	if request.method == 'POST':
		account = request.POST.get('account')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		if password2 != password :
			messages.error(request,'密碼確認錯誤')
		else:
			User.objects.create_user(account,"",password2)
			return redirect('')
	return render(request,'register.html')	
def main(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			logout(request)
			return redirect('')
		return render(request,'main.html')	
	else:
		return render(request,'404notfound.html')	
def hide(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			logout(request)
			return redirect('')
		return render(request,'hide.html')
	else:
		return render(request,'404notfound.html')
def amplification(request):
	if request.user.is_authenticated:
		if request.method =='POST':
			logout(request)
			return redirect('')
		return render(request,'amplification.html')	
	else:
		return render(request,'404notfound.html') 		
def notfound(request):
	return render(request,'404notfound.html')