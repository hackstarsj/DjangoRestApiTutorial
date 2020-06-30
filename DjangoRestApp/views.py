from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from DjangoRestApp.models import Posts
from DjangoRestApp.serializers import PostSerializers

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser == 1:
            return True
        else:
            return False

class PostViewSets(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated,CustomPermission]
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostViewSetsAlternate(viewsets.ViewSet):

    def list(self,request):
        post=Posts.objects.all()
        serializer=PostSerializers(post,many=True,context={"request":request})
        return Response(serializer.data)

    def create(self,request):
        serialier=PostSerializers(data=request.data,context={"request":request})
        serialier.is_valid()
        serialier.save()
        return Response({"error":"False","message":"New Data Created"})

    def update(self,request,pk=None):
        queryset=Posts.objects.all()
        post=get_object_or_404(queryset,pk=pk)
        serializer=PostSerializers(post,data=request.data,context={"request":request})
        serializer.is_valid()
        serializer.save()
        return Response({"error":False,"message":"Data Updated"})

    def retrieve(self,request,pk=None):
        queryset=Posts.objects.all()
        post=get_object_or_404(queryset,pk=pk)
        serializer=PostSerializers(post,context={"request":request})
        return Response({"error":False,"message":"data_return","data":serializer.data})

    def destroy(self,request,pk=None):
        queryset=Posts.objects.all()
        post=get_object_or_404(queryset,pk=pk)
        post.delete()
        return Response({"error":False,"message":"Post Deleted"})

post_list=PostViewSetsAlternate.as_view({"get":"list"})
post_create=PostViewSetsAlternate.as_view({"post":"create"})
post_update=PostViewSetsAlternate.as_view({"put":"update"})
post_retrieve=PostViewSetsAlternate.as_view({"get":"retrieve"})
post_destroy=PostViewSetsAlternate.as_view({"delete":"destroy"})