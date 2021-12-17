from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

from . import forms
from .forms import Banglore, chennai
from .models import addTeam, mumbai, punjab, rajasthan, kolkata, delhi, hyderabad, addNewPlayers
from .serializers import BangloreSerializer, ChennaiSerializer, MumbaiSerializer, DelhiSerializer, PunjabSerializer, \
    RajasthanSerializer, KolkataSerializer, HyderabadSerializer


# Create your views here.

def home(request):
    return render(request, 'MyApp/home.html')

# -------------------------------------------------------------Banglore--------------------------------------------


class BangloreViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = Banglore.objects.all()
        serializer = BangloreSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = Banglore.objects.all(id = id)
            serializer = BangloreSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = BangloreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def bangalore(request):
    if request.method == 'GET':
        playerlist = Banglore.objects.all()
        return render(request, 'MyApp/royalchallenger.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.BangaloreForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')

        else:
            form = forms.BangaloreForm()
        return render(request, 'MyApp/royalchallenger.html', {'form': form})


# ------------------------------------------------------CHENNAI-----------------------------------------------------------


class ChennaiViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = chennai.objects.all()
        serializer = ChennaiSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = chennai.objects.all(id = id)
            serializer = ChennaiSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = ChennaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def Chennai(request):
    if request.method == 'GET':
        playerlist = chennai.objects.all()
        return render(request, 'MyApp/chennai.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.ChennaiForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.ChennaiForm()
        return render(request, 'MyApp/chennai.html', {'form': form})

    # ----------------------------------------------------MUMBAI-------------------------------------------------

class MumbaiViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = mumbai.objects.all()
        serializer = MumbaiSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = mumbai.objects.all(id = id)
            serializer = MumbaiSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = MumbaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)


def Mumbai(request):
    if request.method == 'GET':
        playerlist = mumbai.objects.all()
        return render(request, 'MyApp/mumbai.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.MumbaiForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.MumbaiForm()
        return render(request, 'MyApp/mumbai.html', {'form': form})


# ---------------------------------------------------------------DELHI-------------------------------------------

class DelhiViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = delhi.objects.all()
        serializer = DelhiSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = delhi.objects.all(id = id)
            serializer = DelhiSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = DelhiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def Delhi(request):
    if request.method == 'GET':
        playerlist = delhi.objects.all()
        return render(request, 'MyApp/delhi.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.DelhiForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.DelhiForm()
        return render(request, 'MyApp/delhi.html', {'form': form})



# ----------------------------------PUNJAB--------------------------------------------------------------------

class PunjabViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = punjab.objects.all()
        serializer = PunjabSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = Punjab.objects.all(id = id)
            serializer = PunjabSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = PunjabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def Punjab(request):
    if request.method == 'GET':
        playerlist = punjab.objects.all()
        return render(request, 'MyApp/punjab.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.PunjabForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.PunjabForm()
        return render(request, 'MyApp/punjab.html', {'form': form})

# ---------------------------------------------------------RAJASTHAN---------------------------------------------

class RajasthanViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = rajasthan.objects.all()
        serializer = RajasthanSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = rajasthan.objects.all(id = id)
            serializer = RajasthanSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = RajasthanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def Rajasthan(request):
    if request.method == 'GET':
        playerlist = rajasthan.objects.all()
        return render(request, 'MyApp/rajasthan.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.RajasthanForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.RajasthanForm()
        return render(request, 'MyApp/rajasthan.html', {'form': form})

    # ---------------------------------------------Kolkata---------------------------------------------------------


class KolkataViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = kolkata.objects.all()
        serializer = KolkataSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = Banglore.objects.all(id = id)
            serializer = KolkataSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = KolkataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)

def Kolkata(request):
    if request.method == 'GET':
        playerlist = kolkata.objects.all()
        return render(request, 'MyApp/kolkata.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.KolkataForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.KolkataForm()
        return render(request, 'MyApp/kolkata.html', {'form': form})

    # -------------------------------------------------------------hyderabad------------------------------------


class HyderabadViewset(viewsets.ViewSet):
    def list(self, request):
        playerlist = hyderabad.objects.all()
        serializer = HyderabadSerializer(playerlist, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None ):
        id = pk
        if id is None:
            Playerlist = hyderabad.objects.all(id = id)
            serializer = HyderabadSerializer(Playerlist, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = HyderabadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'data created'}, status=status.HTTP_404_NOT_FOUND)


def Hyderabad(request):
    if request.method == 'GET':
        playerlist = hyderabad.objects.all()
        return render(request, 'MyApp/hyderabad.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.HyderabadForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.HyderabadForm()
        return render(request, 'MyApp/hyderabad.html', {'form': form})


def detail(request):
    return render(request, 'MyApp/detail.html')  


def addPlayers(request):
    if request.method == 'GET':
        playerlist = addNewPlayers.objects.all()
        return render(request, 'MyApp/addnewplayers.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.AddNewPlayers(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')
        else:
            form = forms.AddNewPlayers()
        return render(request, 'MyApp/addnewplayers.html', {'form': form})


def addteam(request):
    if request.method == 'GET':
        playerlist = addTeam.objects.all()
        return render(request, 'MyApp/addteam.html', {'playerlist': playerlist})
    else:
        if request.method == 'POST':
            form = forms.AddNewTeam(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('thanks')
                return render(request, 'MyApp/thanks.html')

        else:
            form = forms.AddNewTeam()
        return render(request, 'MyApp/addteam.html', {'form': form})

def thanks(request):
    return  render(request, 'MyApp/thanks.html')


def SearchTeam(request, name__contains=None):
    if request.method == 'POST':
        searched = request.POST['searched']
        team = addTeam.objects.filter(name__contains= searched)
        
        return render(request, 'MyApp/search.html', {'searched': searched , 'team': team})
    else:
        return render(request, 'MyApp/search.html')
