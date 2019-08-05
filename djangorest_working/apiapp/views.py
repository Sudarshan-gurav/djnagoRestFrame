from django.shortcuts import render

from rest_framework import generics , permissions
from .serializers import BucketlistSerializer,UserSerializer
from .models import Bucketlist
from .permissions import IsOwner
from django.contrib.auth.models import User
from django.views.generic import TemplateView

''' 
     The ListCreateAPIView is a generic view which provides GET (list all) 
     and POST method handlers
'''

class HomePageView(TemplateView):
    template_name = 'home.html'

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)


    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

'''
queryset and serializer_class attributes. 
We also declare a perform_create method that aids in saving a new bucketlist once posted
'''

#---------------------------------------------------------------------------------------
'''
RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), 
PUT, PATCH and DELETE method handlers.

'''

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
    
class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
