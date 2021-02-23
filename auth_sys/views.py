from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserProfile
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('main:main')

    return render(request, "sign_in.html")


def sign_in_handler(request):
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
            return redirect("main:main")
        else:
            return render(request, "sign_in.html", {
                'login_error': "incorrect authorization data"
            })


def log_out(request):
    auth.logout(request)
    return redirect("auth_sys:sign_in")


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/auth/sign_in/'
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "sign_up.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        return super().form_valid(form)
