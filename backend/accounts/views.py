from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import ( 
    reverse_lazy, reverse
)
from django.shortcuts import (
    render, redirect
)

from django.contrib.auth.views import (
    LoginView
)

# Create your views here.
# register, login, logout

from accounts.forms import (
    CustomUserCreationForm, CustomLoginForm, CustomRegisterForm
)


# NOT USED
class CustomRegisterView(View):
    form_class = CustomRegisterForm
    initial = {'key': "value"}
    template_name = "registration/signup.html"

    # block accesss to this page for already logged in users
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        
        # else process dispatch as it otherwise normally would
        return super(CustomRegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='accounts_login')
        return render(request, self.template_name, {'form': "form"})



# NOT USED
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        return super(CustomLoginView, self).form_valid(form)




def signup_view(request: HttpRequest):
    if request.user.is_authenticated:
        messages.info(request, "You have already signed up.")
        return redirect(reverse("home:index"))
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request=request, message=f"Account successfully created with email: {email}")
            return redirect(reverse('login'))
        else:
            return render(request, template_name='registration/signup.html', context={'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name="registration/signup.html", context={'form': form})



def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You have already logged in.")
        return redirect(reverse('home:index'))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Successful login")
            return redirect(reverse('home:index'))
        if user is None:
            messages.error(request, "Invalid Credentials")
            return redirect(reverse('login'))
    else:
        form = CustomLoginForm()
        return render(request, template_name='registration/login.html', context={'form': form})



def logout_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('home:index'))
    else:
        messages.error(request, "You are not logged in.")
        return redirect(reverse('home:index'))