from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/sign_in/')
def main(request):
    return render(request, 'main.html', {'userprofile': request.user.userprofile})
