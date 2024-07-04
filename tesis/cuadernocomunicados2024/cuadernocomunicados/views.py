from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from cuadernocomunicados.forms import RegisterForm
from django.contrib import messages
from cuadernocomunicados.models import Student 
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        user = Student.objects.get(username=request.user.id)
        print(user.dni)
        return render(request, 'index.html', {'data':user})
    else:
        return redirect('loadLogin')

def loadRegister(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm(request.POST)
        if request.method == 'POST':
            if register_form.is_valid():
                    register_form.save()
                    dni = request.POST.get('dni')
                    nroCarnet = request.POST.get('nroCarnet')
                    choice = request.POST.get('tipo')
                    print(nroCarnet)
                    print(dni)
                    try:
                        lastId = User.objects.latest('id')
                        student = Student(dni=dni,nroCarnet=nroCarnet, username=lastId.id, vista=choice) 
                        student.save()
                        messages.success(request, 'Te registraste correctamente')
                    except error:
                        print(error)
                    
                    return redirect('index')

        return render(request,'register.html', {'register_form':register_form})

def loadLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('username')
            pw = request.POST.get('password')
            user = authenticate(request, username=user ,  password=pw )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'Datos ingresados incorrectos.')
                return render(request,'login.html')

        return render(request, 'login.html')

def loadLogOut(request):
    logout(request)
    return redirect('loadLogin')