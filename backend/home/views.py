from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home/index.html')