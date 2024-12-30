from django.shortcuts import render
from .models import Note
from rest_framework.response import Response
from .serializers import NoteSerializer

# Create your views here.

def notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)