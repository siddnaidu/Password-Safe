from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .models import Account, Profile
from .forms import AccountForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def home(request):
    profile = request.user.profile
    accounts = Account.objects.filter(profile=profile)
    context = {'accounts': accounts}
    return render(request, 'password/home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def account_creation(request):
    profile = request.user.profile
    context = {}
    if request.method == 'POST':
        account_form = AccountForm(request.POST)
        context['account_form'] = account_form
        print("here")
        if account_form.is_valid():
            print("there")
            create_account = account_form.save(commit=False)
            create_account.profile = profile
            create_account.save()
            account_pk = create_account.id
            note = 'Account has been created'
            context['note'] = note
        else:
            account_pk = None
        context['account_pk'] = account_pk
        return render(request, 'password/account_creation.html', context)
    else:
        account_form = AccountForm()
        context['account_form'] = account_form
        return render(request, 'password/account_creation.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def account(request, account_id):
    account = Account.objects.get(pk=account_id)
    account_form = AccountForm(instance=account)
    context = {'account_form': account_form, 'account': account}
    if request.method == 'POST':
        filled_account_form = AccountForm(request.POST, instance=account)
        if filled_account_form.is_valid():
            filled_account_form.save()
            note = "Account has been updated"
            context['account_form'] = filled_account_form
            context['note'] = note
            return render(request, 'password/account.html', context)
    return render(request, 'password/account.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Profile.objects.create(
                user = user,
            )
            messages.success(request, f'Account was created for {user_name}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'password/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    context = {}
    return render(request, 'password/login.html', context)

def logOutUser(request):
    logout(request)
    return redirect('login')