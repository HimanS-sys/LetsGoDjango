from django.shortcuts import HttpResponse, render, redirect
from myapp.models import Profile 

# Create your views here
def welcome(request):
    return HttpResponse("Customise welcome page.")

def hello_world(request):
    return HttpResponse("Welcome to the exciting world of Django!")

def profile_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        Profile.objects.create(name=name)
        return redirect('profile')
    else:
        stored_names = Profile.objects.all()
        context = {'stored_names': stored_names}
        return render(request, 'profile.html', context)