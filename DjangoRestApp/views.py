from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from DjangoRestApp.models import Posts
from DjangoRestApp.serializers import PostSerializers


class PostViewSets(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
