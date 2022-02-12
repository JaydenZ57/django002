from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home2.html', {"info": "My name is Jayden, I like python, this is step 2"})