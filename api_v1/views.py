from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from auth_sys.models import Point
from django.contrib.auth.decorators import login_required
from json import loads
from auth_sys.models import Point


# Create your views here.
@login_required(login_url='/auth/sign_in/')
def get_points(request):
    return JsonResponse({'points': Point.get_points()})


@login_required
def new_point(request):
    point = loads(request.POST.get('point'))
    Point.objects.create(x=point['x'], y=point['y'], user=request.user.userprofile)
    return HttpResponse()

