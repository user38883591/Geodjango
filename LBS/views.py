from django.shortcuts import render,redirect
from .models import Facilities_Nairobi
from.models import Schools_Nairobi
from django.http import JsonResponse
from geopy.distance import geodesic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout




# defining the home page
def index(request):
    facilities = list(Facilities_Nairobi.objects.values('facility_name','latitude','longitude')[:70])
    # contex = {'facilities':facilities}
    schools = list(Schools_Nairobi.objects.values('school_name','latitude','longitude'))
    contex = {'facilities':facilities,'schools':schools}
    return render(request,'index.html', contex)
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        try:
            # Attempt to create a new user
            myuser = User.objects.create_user(username=username, password=password, email=email)
            myuser.save()
            messages.success(request, 'You have been signed up successfully.')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the desired page after successful signup
            else:
                messages.error(request, 'Failed to authenticate user after signup.')
                return redirect('index')  # Redirect to the desired page after unsuccessful signup
        except Exception as e:
            # Handle any potential errors during user creation
            messages.error(request, f'Error occurred: {e}')
            return redirect('index')  # Redirect to the desired page after error during signup

    else:
        return render(request, 'signup.html')
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')

def get_features(request):
    if request.method == 'GET':
        latitude = float(request.GET.get('latitude'))
        longitude = float(request.GET.get('longitude'))

        # Query schools and hospitals within the circle
        schools = Schools_Nairobi.objects.all()
        facilities = Facilities_Nairobi.objects.all()

        features = []
        for school in schools:
            if geodesic((latitude, longitude), (school.latitude, school.longitude)).km <= 2.5:
                features.append({'name': school.school_name, 'latitude': school.latitude, 'longitude': school.longitude})

        for facility in facilities:
            if geodesic((latitude, longitude), (facility.latitude, facility.longitude)).km <= 2.5:
                features.append({'name': facility.facility_name, 'latitude': facility.latitude, 'longitude': facility.longitude})

        return JsonResponse(features, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

            
        
# defining the nearest_facility
# def nearest_facility(request):
#     facility_name = request.GET.get('facility_name')
#     latitude = request.GET.get('latitude')
#     longitude = request.GET.get('longitude')


#     if latitude is None or longitude is None:
#         return JsonResponse({'error': 'Latitude and longitude parameters are required'}, status=400)

#     user_location = (float(latitude), float(longitude))

#     # variables  storing nearest facility coordinates and distance
#     nearest_facility_coord = None
#     nearest_facility_name = None
#     nearest_distance = float('inf')  # Initialize with a large value

#     # Iterating through all facilities to find the nearest one
#     for facility in Facilities_Nairobi.objects.all():
#         facility_location = (facility.latitude, facility.longitude)
#         distance = geodesic(user_location, facility_location).km
#         if distance < nearest_distance:
#             nearest_distance = distance
#             nearest_facility_coord = facility_location
#             nearest_facility_name = facility.facility_name

#     return JsonResponse({
#         'coordinates': nearest_facility_coord,
#         'facility_name':nearest_facility_name,
#         'distance': nearest_distance
#     })




# Create your views here.








