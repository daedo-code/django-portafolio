from django.shortcuts import render, redirect
from mensajes.forms import LoginForm, MensajeForm
from mensajes.models import Mensaje
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import redirect

def login_or_home_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('portfolio')  # el nombre de tu url del home
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def portfolio(request):
  if request.method == "POST":
    form = MensajeForm(request.POST)
    if form.is_valid():
        form.save()  # Guarda el mensaje en la base de datos
        return redirect('gracias')  # Redirige a una página de éxito
  else:
    form = MensajeForm()

  return render(request, 'portfolio/home.html',{
    "form":form
  })


def agradecimientos(request):
    return render(request, 'portfolio/gracias.html')


@login_or_home_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_envio')
    return render(request, 'portfolio/mensajes.html', {
       'mensajes': mensajes
    })

# USUARIOS
def signin(request):
    if request.user.is_authenticated:
        return redirect('mensajes')
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("mensajes")
    else:
        form = LoginForm()
    return render(request, "portfolio/login.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return redirect("signin")


