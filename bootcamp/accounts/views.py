from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()
def register_view(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        # import pdb; pdb.set_trace()
        # user = User.objects.create_user(username, email, password)
        try:
            user = User.objects.create_user(username, email, password, is_staff=True)
        except:
            user = None

        if user != None:
            login(request, user)

            return redirect("/")
        else:
            request.session['register_error'] = 1


    # import pdb; pdb.set_trace()


    return render(request, 'accounts/forms.html',
            {'form':form}
            )


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username,
                            password=password
                            )
        print(request, username, password)
        if user:
        
            login(request, user)
            # return redirect("products/")
            return render(request, 'products/detail.html')
            # attemt = request.session.get('attempt') or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            # request.session['invalid_user'] =     1
            # return render(request, 'accounts/forms.html',
            # {'form':form}
            # )

        else:
            request.session['invalid_user'] = 1

    return render(request, 'accounts/forms.html',
            {'form':form}
            )

def logout_view(request):
    logout(request)
    return redirect("/login")