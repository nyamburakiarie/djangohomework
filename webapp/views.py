from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'aboutpage.html')