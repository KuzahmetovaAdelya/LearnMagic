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
        print(db_user.password)
        acception = bcrypt.checkpw(password.encode(), db_user.password.encode())
        if acception:
            if db_user.role == "0":
                return redirect("desktop-child")
            elif db_user.role == "1":
                return redirect("desktop-pup")
            else:
                return HttpResponse(db_user.role)
        else:
            return redirect("auth")
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
            user.password = password.decode()
            user.role = role
            user.save()
            if role == "1":
                return redirect("desktop-pup")
            else:
                return redirect("desktop-child")
    else:
        return render(request, 'main/reg.html')  


def desktopChild(request):
    return render(request, 'main/basic-page.html')


def desktopPup(request):
    return render(request, 'main/basic-page-pup.html')


def gamesPageChild(request):
    return render(request, 'main/all-games.html')


def gamesPagePup(request):
    return render(request, 'main/all-games-pup.html')


def childGameOne(request):
    if request.method == "POST":
        u_answer = request.POST.get("u_answer", "0")
        r_answer = "3"
        if u_answer == r_answer:
            server = {"server": "yes"}
            return render(request, 'main/game-one.html', server)
        else:
            server = {"server": "no"}
            return render(request, 'main/game-one.html', server)
    else:
        return render(request, 'main/game-one.html')


def childGameTwo(request):
    if request.method == "POST":
        u_answer_one = request.POST.get("answer-one", "0").lower()
        u_answer_two = request.POST.get("answer-two", "0").lower()
        u_answer_three = request.POST.get("answer-three", "0").lower()
        u_answer_four = request.POST.get("answer-four", "0").lower()
        r_answer_one = "зеленый"
        r_answer_two = "синий"
        r_answer_three = "желтый"
        r_answer_four = "красный"
        if u_answer_one == r_answer_one and u_answer_two == r_answer_two and u_answer_three == r_answer_three and u_answer_four == r_answer_four:
            server = {"server": "yes"}
            return render(request, 'main/game-two.html', server)
        else:
            server = {"server": "no"}
            return render(request, 'main/game-two.html', server)
    else:
        return render(request, 'main/game-two.html')