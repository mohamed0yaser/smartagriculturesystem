from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/project/smartagrisystem/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of project'
        },
        {
            'Endpoint': '/project/smartagrisystem/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single project object'
        },
        {
            'Endpoint': '/project/smartagrisystem/create/',
            'method': 'POST',
            'body': {'body':""},
            'description': 'create new project with data sent in post request'
        },
        {
            'Endpoint': '/project/smartagrisystem/update/',
            'method': 'PUT',
            'body': {'body':""},
            'description': 'create an existing project with data sent in post request'
        },
        {
            'Endpoint': '/project/smartagrisystem/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete and exiting project'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note =Note.objects.get(id=pk)
    serializer = NoteSerializer(note, request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
