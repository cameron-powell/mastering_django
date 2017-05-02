from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import datetime, timedelta


def hello(request):
    return HttpResponse("Hello world")


def my_homepage_view(request):
    return HttpResponse("Homepage")


def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    html = "In %s hour(s) it will be %s" % (offset, dt)
    return HttpResponse(html)
