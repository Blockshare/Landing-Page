from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from two1.bitserv.django import payment


def index(request):
    return render(request, '../templates/index.html', status=200)


@api_view(['GET'])
@payment.required(5)
def buy(request):
    return HttpResponse('Hello Casey!', status=200)
