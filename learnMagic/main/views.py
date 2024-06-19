from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Persons, Answer
import bcrypt
from django.core.exceptions import ObjectDoesNotExist


def encodeCookie(name, role):
    return f'{name}-{role}'


def decodeCookie(cookie):
    cookie_data = cookie.split("-")
    return cookie_data

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
                response = redirect("desktop-child")
                response.set_cookie('user', encodeCookie(name, db_user.role))
                return response
            elif db_user.role == "1":
                response = redirect("desktop-pup")
                response.set_cookie('user', encodeCookie(name, db_user.role))
                return response
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
                response = redirect("desktop-pup")
                response.set_cookie('user', encodeCookie(name, role))
                return response
            else:
                response = redirect("desktop-child")
                response.set_cookie('user', encodeCookie(name, role))
                return response
    else:
        return render(request, 'main/reg.html')  


def desktopChild(request):
    role = 'Дошкольник'
    name = decodeCookie(request.COOKIES['user'])[0]
    server = {"role": role, "name": name}
    
    return render(request, 'main/basic-page.html', server)



def desktopPup(request):
    role = 'Школьник'
    name = decodeCookie(request.COOKIES['user'])[0]
    server = {"role": role, "name": name}
    return render(request, 'main/basic-page-pup.html', server)


def gamesPageChild(request):
    role = 'Дошкольник'
    name = decodeCookie(request.COOKIES['user'])[0]
    server = {"role": role, "name": name}
    return render(request, 'main/all-games.html', server)


def gamesPagePup(request):
    role = 'Школьник'
    name = decodeCookie(request.COOKIES['user'])[0]
    server = {"role": role, "name": name}
    return render(request, 'main/all-games-pup.html', server)


def childGameOne(request):
    role = 'Дошкольник'
    name = decodeCookie(request.COOKIES['user'])[0]
    if request.method == "POST":
        u_answer = request.POST.get("u_answer", "0")
        game_name = 'Icons'
        r_answer = Answer.objects.get(gameName = game_name).answer
        
        if u_answer == r_answer:
            server = {"server": "yes", "role": role, "name": name}
            return render(request, 'main/game-one.html', server)
        else:
            server = {"server": "no", "role": role, "name": name}
            return render(request, 'main/game-one.html', server)
    else:
        server = {"role": role, "name": name}
        return render(request, 'main/game-one.html', server)


def childGameTwo(request):
    role = 'Дошкольник'
    name = decodeCookie(request.COOKIES['user'])[0]
    if request.method == "POST":
        u_answer_one = request.POST.get("answer-one", "0").lower()
        u_answer_two = request.POST.get("answer-two", "0").lower()
        u_answer_three = request.POST.get("answer-three", "0").lower()
        u_answer_four = request.POST.get("answer-four", "0").lower()
        u_answer = u_answer_one + ", " + u_answer_two + ", " + u_answer_three + ", " + u_answer_four

        game_name = 'Colors'
        r_answer = Answer.objects.get(gameName = game_name).answer

        if u_answer == r_answer:
            server = {"server": "yes", "role": role, "name": name}
            return render(request, 'main/game-two.html', server)
        else:
            server = {"server": "no", "role": role, "name": name}
            return render(request, 'main/game-two.html', server)
    else:
        server = {"role": role, "name": name}
        return render(request, 'main/game-two.html', server)
    

def pupGameOne(request):
    role = 'Школьник'
    name = decodeCookie(request.COOKIES['user'])[0]
    if request.method == "POST":
        game_name = 'Situation'
        r_answer = Answer.objects.get(gameName = game_name).answer

        answer = request.POST.get("n", "0")
        if answer == r_answer:
            server = {"server": "yes", "role": role, "name": name}
            return render(request, 'main/game-three.html', server)
        else:
            server = {"server": "no", "role": role, "name": name}
            return render(request, 'main/game-three.html', server)
    else:
        server = {"role": role, "name": name}
        return render(request, 'main/game-three.html', server)


def pupGameTwo(request):
    role = 'Школьник'
    name = decodeCookie(request.COOKIES['user'])[0]
    if request.method == "POST":

        game_name = 'IT'
        r_answer = Answer.objects.get(gameName = game_name).answer

        answer = request.POST.get("n", "0")
        if answer == r_answer:
            server = {"server": "yes", "role": role, "name": name}
            return render(request, 'main/game-four.html', server)
        else:
            server = {"server": "no", "role": role, "name": name}
            return render(request, 'main/game-four.html', server)
    else:
        server = {"role": role, "name": name}
        return render(request, 'main/game-four.html', server)
    

def exit(request):
    response = redirect("startPage")
    response.delete_cookie('user')
    return response


def profile(request):
	name = decodeCookie(request.COOKIES['user'])[0]
	if decodeCookie(request.COOKIES['user'])[1] == '1':
		role = 'Школьник'
	else:
		role = 'Дошкольник'
	
	server = {'name':name, 'role':role}
	return render(request, 'main/profile.html', server)


def home(request):
	if decodeCookie(request.COOKIES['user'])[1] == '1':
		response = redirect("desktop-pup")
	else:
		response = redirect("desktop-child")

	return response


def changeProfile(request):
    if request.method == 'POST':
        action = request.POST.get('action', 'nameChange')
        name = decodeCookie(request.COOKIES['user'])[0]
        user = Persons.objects.get(name = name)
        if action == 'nameChange':
            newName = request.POST.get('name', 'Undefined')
            user.name = newName
            user.save(update_fields=['name'])
            response = redirect('profile')
            response.set_cookie('user', encodeCookie(newName, user.role))
        elif action == 'roleChange':
            newRole = request.POST.get('role', '0')
            user.role = newRole
            user.save(update_fields=['role'])
            response = redirect('profile')
            response.set_cookie('user', encodeCookie(name, newRole))
        else:
            newPassword = request.POST.get('password', 'None')
            newPassword = bcrypt.hashpw(newPassword.encode(), bcrypt.gensalt())
            user.password = newPassword.decode()
            user.save(update_fields=['password'])
            response = redirect('profile')

        return response
    else:
        name = decodeCookie(request.COOKIES['user'])[0]
        if decodeCookie(request.COOKIES['user'])[1] == '1':
            role = 'Школьник'
        else:
            role = 'Дошкольник'     
        server = {'name':name, 'role':role}
        return render(request, 'main/profile-change.html', server)
           