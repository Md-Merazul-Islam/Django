
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from .forms import CustomUserCreationForm
# Create your views here.


class RegisterView (FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        user = form.instance
        login(self.request, user)
        messages.success(
            self.request, f'Account created fo {username} successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, f'Register failed! ')
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, f'Logged successfully. ')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, f'Invalid username or password. ')
        return super().form_invalid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('user_login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return super().get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'
