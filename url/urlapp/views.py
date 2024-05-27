from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UrlSerializer
from django.utils.http import urlsafe_base64_encode
from rest_framework.response import Response
# from rest_framework.red
from rest_framework import status
from .models import UrlModel
from django.http import HttpResponseRedirect
# from rest_framework.

@api_view(["POST"])
def index(request):

    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        instance.short_url = urlsafe_base64_encode(str(instance.id).encode("utf-8"))
        instance.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def get_actual_url(request,url):
    u = UrlModel.objects.get(short_url=url)
    return HttpResponseRedirect(u.url)    
