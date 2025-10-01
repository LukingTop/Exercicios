from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.template import loader
from meusite.pessoa import Pessoa

def get_user_home_name(user):
    if user.is_superuser:
        return 'admin_dashboard'
    if user.groups.filter(name='Gerente').exists() or user.is_staff:
        return 'manager_dashboard'
    return 'user_dashboard'

def home(request):
    return render(request, 'index.html', {'user': request.user})

def pessoas_list(request):
    pessoas = Pessoa.objects.select_related('user').prefetch_related('endereco_set').all()
    return render(request, 'People.html', {'pessoas': pessoas})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(get_user_home_name(user))
        messages.error(request, "Usuário ou senha incorretos.")
    return render(request, 'Login.html')

def logout_view(request):

    logout(request)
    messages.info(request, "Você saiu com sucesso.")
    return render(request, 'Logout.html')

def recover_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Informe o e-mail.")
            return render(request, 'Recover.html')

        try:
            user = User.objects.get(email=email)
            messages.success(request,)
        except User.DoesNotExist:
            messages.success(request,)
        return render(request, 'Recover.html')

    return render(request, 'Recover.html')

def change_password_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "Faça login para alterar a senha.")
        return redirect('login')

    if request.method == 'POST':
        current = request.POST.get('current_password')
        new1 = request.POST.get('new_password1')
        new2 = request.POST.get('new_password2')

        if not request.user.check_password(current):
            messages.error(request, "Senha atual incorreta.")
            return render(request, 'ChangePassword.html')

        if new1 != new2:
            messages.error(request, "As senhas novas não coincidem.")
            return render(request, 'ChangePassword.html')

        try:
            validate_password(new1, user=request.user)
        except ValidationError as e:
            for msg in e:
                messages.error(request, msg)
            return render(request, 'ChangePassword.html')

        request.user.set_password(new1)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.success(request, "Senha alterada com sucesso.")
        return redirect(get_user_home_name(request.user))

    return render(request, 'ChangePassword.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if not username or not email or not password1:
            messages.error(request, "Preencha todos os campos.")
            return render(request, 'Register.html')

        if password1 != password2:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'Register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return render(request, 'Register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return render(request, 'Register.html')

        try:
            validate_password(password1, user=None)
        except ValidationError as e:
            for msg in e:
                messages.error(request, msg)
            return render(request, 'Register.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        messages.success(request, "Conta criada com sucesso. Você está logado.")
        return redirect(get_user_home_name(user))

    return render(request, 'Register.html')

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'Profile.html', context)

@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    return render(request, 'AdminDashboard.html')

@login_required(login_url='login')
def manager_dashboard(request):
    if not (request.user.groups.filter(name='Gerente').exists() or request.user.is_staff):
        raise PermissionDenied
    return render(request, 'ManagerDashboard.html')

@login_required(login_url='login')
def user_dashboard(request):
    return render(request, 'UserDashboard.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_403_view(request, exception=None):

    return render(request, '403.html', status=403)

def custom_500_view(request):

    return render(request, '500.html', status=500)




