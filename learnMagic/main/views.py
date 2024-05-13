from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Persons
import bcrypt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'main/start-page.html')

# For render auth page
def auth(request):
    if request.method == "POST":
        
        name = request.POST.get('name', 'Undefined')
        password = request.POST.get('password', 'None')

        db_user = Persons.objects.get(name=name)

        db_password = bcrypt.checkpw(password.encode(), db_user.password)
        return HttpResponse(f'<p>{db_password}, {password}</p>')
        # if db_pass == password:
        #     redirect("desktop")
        # else:
        #     redirect("auth")
    else:
        return render(request, 'main/auth.html')


# For render reg page
def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Undefined')
        password = request.POST.get('password', '1')
        password_again = request.POST.get('passwordAgain', '0')
        role = request.POST.get('role', '0')

        if password == password_again:
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            user = Persons()
            user.name = name
            user.password = password
            user.role = role
            user.save()
            return redirect("desktop")
    else:
        return render(request, 'main/reg.html')  


def desktop(request):
    return render(request, 'main/basic-page.html')


def gamesPage(request):
    return render(request, 'main/all-games.html')