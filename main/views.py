from gc import get_objects
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import FactionMember, Faction
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FactionMemberSerializer

def members_list(request):
    members = FactionMember.objects.all()
    return render(request, 'members.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(FactionMember, id=id)
    return render( request, 'member_detail.html',{'member': member})

@login_required(login_url='login_user')
def add_member(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('members_list')

    else:
        form = MemberForm()

    return render(request, 'add_member.html', {'form': form})

@login_required(login_url='login_user')
def edit_member(request, id):
    member = get_object_or_404(FactionMember, id=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return redirect('member_detail', id=member.id)

    else:
        form = MemberForm(instance=member)

    return render(request, 'edit_member.html', {'form': form})

@login_required(login_url='login_user')
def delete_member(request, id):
    member = get_object_or_404(FactionMember, id=id)

    if request.method == 'POST':
        member.delete()

        return redirect('members_list')
    return render(request, 'delete_member.html', {'member': member})

def login_user(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('members_list')
        else:
            error = 'Неверный логин или пароль'

    return render(request, 'login.html', {'error': error})

def logout_user(request):
    logout(request)
    return redirect('members_list')

def faction_detail(request, id):
    faction = get_object_or_404(Faction, id=id)
    members = FactionMember.objects.filter(faction=faction)

    return render(request, 'faction_detail.html', {
        'faction': faction,
        'members': members
    })

@api_view(['GET', 'POST'])
def api_members_list(request):

    if request.method == 'GET':
        members = FactionMember.objects.all()
        serializer = FactionMemberSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FactionMemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def api_member_detail(request, id):

    member = get_object_or_404(FactionMember, id=id)

    if request.method == 'GET':
        serializer = FactionMemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FactionMemberSerializer(member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == 'DELETE':
        member.delete()
        return Response({'message': 'Участник удалён'})