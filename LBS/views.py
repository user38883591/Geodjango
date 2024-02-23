from django.shortcuts import render
from .models import Facilities_Nairobi
from django.http import JsonResponse
from geopy.distance import geodesic
# defining the home page
def index(request):
    facilities = list(Facilities_Nairobi.objects.values('facility_name','latitude','longitude')[:70])
    contex = {'facilities':facilities}
    return render(request,'index.html', contex)

# defining the nearest_facility
def nearest_facility(request):
    facility_name = request.GET.get('facility_name')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')


    if latitude is None or longitude is None:
        return JsonResponse({'error': 'Latitude and longitude parameters are required'}, status=400)

    user_location = (float(latitude), float(longitude))

    # variables  storing nearest facility coordinates and distance
    nearest_facility_coord = None
    nearest_facility_name = None
    nearest_distance = float('inf')  # Initialize with a large value

    # Iterating through all facilities to find the nearest one
    for facility in Facilities_Nairobi.objects.all():
        facility_location = (facility.latitude, facility.longitude)
        distance = geodesic(user_location, facility_location).km
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_facility_coord = facility_location
            nearest_facility_name = facility.facility_name

    return JsonResponse({
        'coordinates': nearest_facility_coord,
        'facility_name':nearest_facility_name,
        'distance': nearest_distance
    })




# Create your views here.








