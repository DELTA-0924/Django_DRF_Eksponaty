from django.shortcuts import render
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import EksponatySerializer,CommentSerializer
from rest_framework.permissions import AllowAny
class ListViewEks(ListCreateAPIView):
    queryset=Eksponaty.objects.all()
    serializer_class=EksponatySerializer
    permission_classes=[AllowAny]
class ListViewComment(ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[AllowAny]
