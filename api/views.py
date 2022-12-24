from django.shortcuts import render
from .serialzers import NoteSerializer,UserSerializer
from django.http import JsonResponse
from .models import Note
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,auth
# Create your views here.
@api_view(['GET'])
def FrontPage(request):
    return Response('Our API')

@api_view(['POST'])
def GetData(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    user_name = request.data['user_name']
    password = request.data['password']
    user = auth.authenticate(username=user_name,password=password)
    request.session['user_name'] = user_name
    AllNotes = Note.objects.filter(user_name=user.id).order_by('-last_updated')
    serializer = NoteSerializer(AllNotes,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET'])
def GetANote(request,id):
    AllNotes = Note.objects.get(id=id)
    return Response(NoteSerializer(AllNotes).data,status = status.HTTP_200_OK)
@api_view(['GET'])
def UserAlreadyInside(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    data = {
        'user_name':request.session.get('user_name')
    }
    return JsonResponse(data,status=status.HTTP_200_OK)
@api_view(['GET'])
def DeleteANote(request,id):
    n = Note.objects.get(id=id)
    n.delete()
    return JsonResponse({'status':'deleted'})

@api_view(['GET'])
def LogoutUser(request):
    request.session.pop('user_name')
    return JsonResponse({'Done'},status=status.HTTP_200_OK)

@api_view(['POST'])
def LoginUser(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    user_name = request.data['user_name']
    password = request.data['password']
    user = auth.authenticate(username=user_name,password=password)

    if user is not None:
        auth.login(request,user)
        return JsonResponse({'status':'Correct'})
    else:
        request.session['user_name'] = user_name
        return JsonResponse({'status':'Incorrect'})
    
@api_view(['GET','POST'])
def RegesterNewUser(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    user_name = request.data['user_name']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']

    user = User.objects.create_user(username=user_name,password=password,email=email,first_name = first_name,last_name=last_name)
    user.save()
    request.session['user_name'] = user_name
    return JsonResponse({'status':'created'})


@api_view(['POST'])
def get_already_login_user(request):
    user_name = request.data['user_name']
    user = User.objects.get(username=user_name)
    return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_new_note(request):
    user_name = request.data['user_name']
    password = request.data['password']
    user = auth.authenticate(username=user_name,password=password)
    note = request.data['note']
    title = request.data['title']
    n = Note(user_name = user, note = note,title = title)
    n.save()
    return JsonResponse({'status':'created'})

@api_view(['POST'])
def update_a_note(request,id):
    n = Note.objects.get(id=id)
    n.note = request.data['note']
    n.title = request.data['title']
    n.save()
    return JsonResponse({'status':'done'})