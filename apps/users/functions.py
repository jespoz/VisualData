
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def loginuser(request, username, password):
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)