from urllib.parse import urlparse
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import is_valid_path
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
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



class CustomRegisterView(View):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    # block accesss to this page for already logged in users
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have already registered.")
            return redirect(to='/')
        
        # else process dispatch as it otherwise normally would
        return super(CustomRegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            return redirect(reverse('accounts:login'))
        return render(request, self.template_name, {'form': form})




class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have already logged in.")
            return redirect(to='/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next_page = self.request.POST['next']
        if next_page == '':
            next_page = '/' # if next param is not available, then redirect the user to the homepage after login.
        return next_page
    
    # def form_valid(self, form: AuthenticationForm) -> HttpResponse:
    #     response = super().form_valid(form)
    #     next_url = self.request.GET.get('next') or self.request.POST.get('next')
    #     if next_url:
    #         return HttpResponseRedirect(f"{self.request.path}?next={next_url}")
    #     return response



# NOT USED
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
            return redirect(reverse('accounts:login'))
        else:
            return render(request, template_name='registration/signup.html', context={'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name="registration/signup.html", context={'form': form})



# NOT USED, Django docs recommended using class based LoginView
def login_view(request):
    next_url = request.GET.get('next', '/')
    if request.user.is_authenticated:
        messages.info(request, "You have already logged in.")
        return redirect(reverse('home:index'))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # ensure next url is safe
            next_url = request.POST.get('next', next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                return HttpResponseRedirect(next_url)
            messages.success(request, "Successful login")
            return redirect(reverse('home:index'))
        if user is None:
            messages.error(request, "Invalid Credentials")
            return redirect(reverse('accounts:login'))
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
    



@login_required
def profile(request: HttpRequest):
    return render(request, template_name='accounts/profile.html')