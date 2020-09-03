from django.shortcuts import render


# Create your views here.

app_name = 'myresume'

def home(request):
	return render(request, 'myresume/index.html')

