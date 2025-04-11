from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import Reg_from

# Create your views here.
def login_user(r):
    login(r)
    print(f'Юзер авторизировался blya')
    return redirect('mainpage')

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