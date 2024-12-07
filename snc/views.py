from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'snc/home.html')


def login(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform your login validation logic (e.g., checking username, password)
        # For now, assume login validation is successful

        # Redirect based on the role selected
        if role == 'admin':
            return redirect('ahome')
        elif role == 'seller':
            return redirect('shome')
        elif role == 'bidder' or role == 'guest':
            return redirect('uhome')
    else:
        return render(request, 'snc/login.html')


def register(request):
    return render(request,'snc/register.html')


def uhome(request):
    return render(request,'snc/uhome.html')



def ahome(request):
    return render(request,'snc/ahome.html')


def shome(request):
    return render(request,'snc/shome.html')


def hcontactus(request):
    return render(request,'snc/hcontactus.html')


def haboutus(request):
    return render(request,'snc/haboutus.html')

def hprivacypolicy(request):
    return render(request,'snc/hprivacypolicy.html')


def hterms(request):
    return render(request,'snc/hterms.html')

def vuharley(request):
    return render(request,'snc/vuharley.html')

def atuser(request):
    return render(request,'snc/atuser.html')


def atauction(request):
    return render(request,'snc/atauction.html')
def alauction(request):
    return render(request,'snc/alauction.html')

def buser1(request):
    return render(request,'snc/buser1.html')


def adharley(request):
    return render(request,'snc/adharley.html')

def adrolex1(request):
    return render(request,'snc/adrolex1.html')
def adthar1(request):
    return render(request,'snc/adthar1.html')

def adlamborghini1(request):
    return render(request,'snc/adlamborghini1.html')

def adwatch1(request):
    return render(request,'snc/adwatch1.html')

def adguitar1(request):
    return render(request,'snc/adguitar1.html')

def adrareart1(request):
    return render(request,'snc/adrareart1.html')

def adsneaker1(request):
    return render(request,'snc/adsneaker1.html')

def adhermesh1(request):
    return render(request,'snc/adhermesh1.html')

def adhondarc30(request):
    return render(request,'snc/adhondarc30.html')
def settings(request):
    return render(request,'snc/settings.html')
def adnecklace1(request):
    return render(request,'snc/adnecklace1.html')
def help(request):
    return render(request,'snc/help.html')
def addadmin(request):
    return render(request,'snc/addadmin.html')

