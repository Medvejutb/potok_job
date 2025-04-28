from django.shortcuts import render, redirect
from django.contrib.auth import logout, login,authenticate
from .forms import Reg_from, Log_form

# Create your views here.
def login_user(r):

    if r.method == 'POST':
        form = Log_form(r.POST)

        if form.is_valid():
            
            name = form.cleaned_data['first_name']
            tg = form.cleaned_data['tg']
            password = form.cleaned_data['password']
            user = authenticate(r, first_name=name, tg=tg, password=password)
            if user is not None:
                login(r, user)
                print(f'Юзер авторизировался blya')
                return redirect('mainpage')
            else:
                form.add_error(None, 'eblan?)')
    else:
        form = Log_form()

    return render(r, 'users/login', {'form': form})

def logout_user(r):
    logout(r)
    print(f'Юзер логаут blya')
    return redirect('mainpage')

def reg(r):
    if r.method == 'POST':
        form = Reg_from(r.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('mainpage')
    else:
        form = Reg_from()

    return render(r, 'users/reg.html', {'form': form})