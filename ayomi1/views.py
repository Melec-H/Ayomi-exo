from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from ayomi1.forms import EditProfileForm

def index(request):
	return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def profile(request):
	args = {'user': request.user}
	return render(request, 'profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'edit_profile.html', args)