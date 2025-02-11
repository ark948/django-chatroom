from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.translation import gettext as _


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home/index.html')


def test_translation(request: HttpRequest) -> HttpResponse:
    output = _("Welcome to this site.")
    return HttpResponse(output)
