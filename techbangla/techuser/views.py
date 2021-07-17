'''from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, ListView, RedirectView
from techuser.forms import RegistrationForm
from django.contrib.auth.models import User
from techuser.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
# Decorator
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


# Registration Class Based
class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy("tech_blog:index")

    def form_valid(self, form):
        valid = super(RegistrationView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


# Registration Functional
# @login_executed('tech_user:author-profile')
# def registrationview(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('tech_blog:index'))
#     data = {
#         'form': form,
#     }
#     return render(request, 'registration.html', context=data)


@login_executed('tech_user:author-profile')
def loginview(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if user:
                    login(request, user)
                    # print('Ok')
                    return HttpResponseRedirect(reverse('tech_blog:index'))
                else:
                    print("Account not active")
            else:
                print("Login Details Wrong")
    data = {
        'form': form,
    }
    return render(request, 'login.html', context=data)


#
# class LoginView(CreateView):
#     form_class = AuthenticationForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('tech_blog:index')

# Logout Class Based
# class LogoutView(RedirectView):
#     # url = 'account/login/'
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)


# Logout Functional
@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('tech_blog:index'))


# class ProfileView(DetailView):
#     model = UserProfile
#     context_object_name = "userprofile"
#     template_name = 'user-profile.html'
#     slug_field = 'pk'


def profileview(request, user_name):
    user = User.objects.get(username=user_name)
    user_profile = UserProfile.objects.get(user=user.pk)
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'user-profile.html', context)
'''

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from techuser.models import UserProfile
from techuser.forms import RegistrationForm, UserBasicChange, UserBasicChange2, UserBasicChange3


# Create your views here.
# Decorator
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


@login_executed('tech_blog:index')
def registrationview(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('tech_blog:index'))
    context = {
        'form': form,
    }
    return render(request, 'registration.html', context)


@login_executed('tech_blog:index')
def loginview(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username, password = request.POST.get('username'), request.POST.get('password')
        # username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password') # Work as above
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tech_blog:index'))
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('tech_blog:index'))


@login_required
def ownprofile(request):
    blogs = User.objects.all()
    return render(request, 'user-profile.html', context={'blogs': blogs})


@login_required
def settingsview(request):
    context = {

    }

    return render(request, 'settings.html', context)

@login_required
def basicsetting(request):
    current_user = request.user
    # form = RegistrationForm(instance=request.user)
    form = UserBasicChange(instance=current_user)
    if request.method == 'POST':
        form = UserBasicChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserBasicChange(instance=current_user)
            return HttpResponseRedirect(reverse('tech_user:ownprofile'))
    context = {
        'form': form,
    }

    return render(request, 'basic-info.html', context)

@login_required
def othersetting(request):
    current_user = request.user
    form = UserBasicChange2(instance=current_user.user_profile)
    if request.method == 'POST':
        form = UserBasicChange2(request.POST, request.FILES, instance=current_user.user_profile)
        if form.is_valid():
            form.save()
            # user_obj.user = current_user
            # user_obj.save()
            form = UserBasicChange2(instance=current_user.user_profile)
            return HttpResponseRedirect(reverse('tech_user:ownprofile'))
    context = {
        'form': form
    }

    return render(request, 'basic-info.html', context)


@login_required
def addprofilepic(request):
    current_user = request.user
    form = UserBasicChange3()
    if request.method == 'POST':
        form = UserBasicChange3(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = current_user
            user_obj.save()
            return HttpResponseRedirect(reverse('tech_user:ownprofile'))
    context = {
        'form': form
    }

    return render(request, 'basic-info.html', context)

@login_required
def changepass(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tech_user:ownprofile'))
    context = {
        'form': form,
    }
    return render(request, 'basic-info.html', context)


def authorprofile(request, username):
    author = User.objects.get(username=username)
    blogs = User.objects.all()
    context = {
        'author': author,
        'blogs': blogs,
    }
    return render(request, 'author-profile.html', context)