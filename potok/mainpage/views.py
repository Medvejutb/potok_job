from django.shortcuts import render

def mainpage(request):
    user = request.user
    user_is_auth = False
    if user.is_authenticated:
        user_is_auth = True
    else:
        user_is_auth = False
    return render(request, 'mainpage/mainpage.html', {'is_auth': user_is_auth})

def inf1(r):
    return render(r,'mainpage/inf1.html')