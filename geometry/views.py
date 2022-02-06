from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import math


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {radius * radius * math.pi}')


def func_rectangle(request, width: int, height: int):
    redirect_url = reverse('rectangle', args=(width, height, ))
    return HttpResponseRedirect(redirect_url)


def func_square(request, width: int):
    redirect_url = reverse('square', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def func_circle(request, radius: int):
    redirect_url = reverse('circle', args=(radius, ))
    return HttpResponseRedirect(redirect_url)
