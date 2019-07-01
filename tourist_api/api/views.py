# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import LocationSerializers, Videos_Location_Serializers, Place_Serializers
from .models import Location, Videos_Location, Place

# Manage places (one city eg)
class Create_Place(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""
    queryset = Place.objects.all()
    serializer_class = Place_Serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# Manage locations from place
class CreateView(generics.ListCreateAPIView):
	
    """This class defines the create behavior of our rest api."""
    # queryset = Location.objects.all()
    serializer_class = LocationSerializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        place_id = self.kwargs['place_id']

        # Filter by location id
        queryset = Location.objects.filter(place__id__exact = place_id).order_by("-id")        

        # Return queryset
        return queryset

# View for videos location
class Create_View_Videos_Location(generics.ListCreateAPIView):
	
    """This class defines the create behavior of our rest api."""
    # queryset = Videos_Location.objects.all()
    serializer_class = Videos_Location_Serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        location_id = self.kwargs['location_id']

        # Filter by location id
        queryset = Videos_Location.objects.filter(location__id__exact = location_id).order_by("-id")
        

        # Return queryset
        return queryset

