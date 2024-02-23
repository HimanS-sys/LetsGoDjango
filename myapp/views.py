from django.shortcuts import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Customise welcome page.")

def hello_world(request):
    return HttpResponse("Welcome to the exciting world of Django!")
