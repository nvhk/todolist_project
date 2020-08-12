from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ToDoFormularz
from .models import ToDosy
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required




# Create your views here.

def home(request):
     return render(request, 'todo/home.html')


def rejestracja(request):
    if request.method == 'GET':
        # Wyswietl Strone
        return render(request, 'todo/rejestracja.html', {'formularz_rejestacji':UserCreationForm()})
    else:
        # Zrob usera


        # Sprawdz hasla
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                #
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #dodaj haslo
                user.save() # zapisz usera do bazy
                login(request, user)
                return render(request, 'todo/rejestracja.html', {'formularz_rejestacji':UserCreationForm(), 'sukces':True}) #zwroc stone z info ze sie udalo

            #przechwyc czy user juz istnieje    
            except IntegrityError:
                return render(request, 'todo/rejestracja.html', {'formularz_rejestacji':UserCreationForm(), 'error':'Taki uzytkownik juz istnieje'})
            
        else:
            return render(request, 'todo/rejestracja.html', {'formularz_rejestacji':UserCreationForm(), 'error':'Hasła sie nie zgadzają'})

@login_required
def todosy(request):
    # todosy = ToDosy.objects.all() - wszytkie
    todosy = ToDosy.objects.filter(user=request.user, wykonanie__isnull=True)
    return render(request, 'todo/todosy.html', {'todosy':todosy})

@login_required
def wyloguj(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def zaloguj(request):

    if request.method == 'GET':
        # Wyswietl Strone z logowaniem
        return render(request, 'todo/login.html', {'formularz_logowania':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'] )

        if user is None:
            return render(request, 'todo/login.html', {'formularz_logowania':AuthenticationForm(), 'error':'złe hasło lub użytnik' })
        
        else:
            login(request, user)
            return redirect('todosy')

@login_required
def dodaj(request):
    if request.method == 'GET':
        return render(request, 'todo/dodaj.html', {'formularz_dodaj':ToDoFormularz()})
    else:
        try:
            formularz = ToDoFormularz(request.POST)
            newtodo = formularz.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todosy')
        except ValueError:
            return render(request, 'todo/dodaj.html', {'formularz_dodaj':ToDoFormularz(), 'error':'cos zle wpisales'})



@login_required
def zobacztodos(request, todosy_pk):
    todo = get_object_or_404(ToDosy, pk=todosy_pk, user=request.user)
    

    if request.method == 'GET':
        form = ToDoFormularz(instance=todo)
        return render(request, 'todo/zobacztodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = ToDoFormularz(request.POST, instance=todo)
            form.save()
            return redirect('todosy')
            
        except ValueError:
            return render(request, 'todo/zobacztodo.html', {'todo':todo, 'form':form, 'error':'cos zle wpisales', 'now':now})




@login_required
def wykonanie(request, todosy_pk):
    todo = get_object_or_404(ToDosy, pk=todosy_pk, user=request.user)

    if request.method == 'POST':
        todo.wykonanie = datetime.datetime.now()
        todo.save()
        return redirect('todosy')

@login_required
def usun(request, todosy_pk):
    todo = get_object_or_404(ToDosy, pk=todosy_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todosy')


@login_required
def zrobione(request):
    # todosy = ToDosy.objects.all() - wszytkie
    zrobione = ToDosy.objects.filter(user=request.user, wykonanie__isnull=False).order_by('-wykonanie')
    return render(request, 'todo/zrobione.html', {'zrobione':zrobione})