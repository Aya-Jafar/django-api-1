
#from django.http import JsonResponse
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NoteSerialzer
from .models import Note


@api_view(http_method_names=['GET'])
def getNotes(request):
    notes = Note.objects.all()
    slz = NoteSerialzer(notes, many=True)
    return Response(data=slz.data)


@api_view(http_method_names=['GET'])
def getNote(request, id):
    note = Note.objects.get(id=id)
    slz = NoteSerialzer(note, many=False)
    return Response(data=slz.data)


@api_view(http_method_names=['POST'])
def createNote(request):
    back_data = request.data
    new_note = Note.objects.create(body=back_data['body'])
    slz = NoteSerialzer(new_note, many=False)
    return Response(data=slz.data)


@api_view(http_method_names=['PUT'])
def updateNote(request,id):
    note = Note.objects.get(id=id)

    slz = NoteSerialzer(note, data=request.data)
    if slz.is_valid():
        slz.save()
        return Response(slz.data)
    return Response(slz.errors)  


@api_view(http_method_names=['DELETE'])
def deleteNote(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response("Note was deleted!")
    