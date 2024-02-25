import json
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from myapp.models import Profile 

# Create your views here
def welcome(request):
    return HttpResponse("Customise welcome page.")

def hello_world(request):
    return HttpResponse("Welcome to the exciting world of Django!")


@csrf_exempt
def profile_view_json(request):
    """
    Description:
    Creates a new profile with the provided information.
    Get the list of profiles already created.

    Parameters:

    POST: 
    name (str): The name of the profile.
    email (str): The email address of the profile.

    GET: None
    """

    if request.method == 'GET':
        profiles = Profile.objects.all()
        data = [{"id": profile.id, 'name': profile.name, 'address': profile.address, 'mobile_number': profile.mobile_number, 'email': profile.email} for profile in profiles]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        if name and email:
            profile = Profile(name=name, address=address, mobile_number=mobile_number, email=email)
            profile.save()
            serialized_obj = serializers.serialize('json', [ profile, ])
            data = json.loads(serialized_obj)
            return JsonResponse({"message" : "Profile created successfully", "data" : data[0]})
        else:
            return JsonResponse({"error_message" : "Name and Email are required fields"}, status=400)

    else:
        return JsonResponse({"message" : "Method not allowed"}, status=405)


def profile_view(request):
    """

    Description:
    Creates a profile with provided informaition.
    Displays the list of profile already created.

    Parameters:

    POST:
    name (str): name of the profile.
    mobile_number (str): mobile number of the profile.
    adderess (str): address of the profile.
    email (str): email address of the profile.

    GET:
    None 

    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        mobile_number = request.POST.get("mobile_number", "")
        address = request.POST.get("address", "")
        email = request.POST.get("email", "")
        if name and email:
            Profile.objects.create(name=name, address=address, mobile_number=mobile_number, email=email)
        else:
            return render(request, 'profile.html', {"error_message": "Name and Email are required fields"})
        return redirect('profile')
    else:
        stored_profiles = Profile.objects.all()
        context = {'stored_profiles': stored_profiles}
        return render(request, 'profile.html', context)
    

def get_profile_by_name(request, name):
    '''
    Description:
    Returns users profile details by name.

    Parameters:

    GET:
    name (str): name of the profile.
    '''
    try:
        profile = Profile.objects.get(name=name)
        user_data = {
            "name" : profile.name,
            "address" : profile.address,
            "mobile_number" : profile.mobile_number,
            "email" : profile.email,
        }
        return JsonResponse(user_data)
    except Profile.DoesNotExist as e:
        error_message = f"Profile '{name}' does not exist: {str(e)}"
        error_data = {"error" : error_message}
        return JsonResponse(error_data, status = 404)

@csrf_exempt
def profile_detail_view(request, pk):
    '''
    Description:
    (GET) Returns details of a perticular profile based on the provided profile key.
    (PUT) Updates name or email address of a perticular profile based on the provided 
    profile key.
    (DELETE) Deletes profile key corresponding to the provided profile key

    Parameters:

    GET, PUT, DELETE:
    pk (int 64): a unique id associated with a profile.

    '''
    if request.method == "GET":
        try:
            profile = Profile.objects.get(id=pk)
            user_data = {"id" : profile.id, "name" : profile.name, "address": profile.address, "mobile_number": profile.mobile_number, "email": profile.email}
            return JsonResponse(user_data)
        except Profile.DoesNotExist as e:
            error_message = f"Profile for id:'{pk}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status=404)
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        try:
            profile = Profile.objects.get(id=pk)
            if {"name", "email"}.issubset(request_params.keys()):
                profile.name = request_params["name"]
                profile.email = request_params["email"]
            elif "name" in request_params:
                profile.name = request_params["name"]
            elif "email":
                profile.email = request_params["email"]
            else:
                return JsonResponse({"error": "Request body cannot be empty"}, status=400)
        except Profile.DoesNotExist as e:
            error_message = f"Profile for id:'{pk}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status=404)
        profile.save()
        user_data = {"id" : profile.id, "name" : profile.name, "address": profile.address, "mobile_number": profile.mobile_number, "email": profile.email}
        return JsonResponse(user_data)
    elif request.method == "DELETE":
        try:
            profile = Profile.objects.get(id=pk)
            profile.delete()
            success_message = f"profile id:'{pk}' deleted successfully"
            return JsonResponse({"message": success_message})
        except Profile.DoesNotExist as e:
            error_message = f"Profile for id:'{pk}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status=404)

        
    else:
        return JsonResponse({"message" : "Method not allowed"}, status=405)


def update_email(request, name):
    '''
    Description:
    Updates email address based on the user's name provided.

    Parameters:

    PUT:
    name (str): name of the profile.

    '''
    if request.method == "PUT":
        try:
            profile = Profile.objects.get(name=name)
            data = json.loads(request.body)
            new_email = data.get("email")
            if new_email:
                profile.email = new_email
                profile.save()
                return JsonResponse({"message" : "Email updated succesfully"})
            else:
                return JsonResponse({"error": "Email not provided in request body"}, status=400)
        except Profile.DoesNotExist as e:
            error_message = f"Profile '{name}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status = 404)
    else:
        return JsonResponse({"error" : "only 'PUT' request are allowed"}, status = 404)