from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})

    """ step 360
    user = request.user
    return HttpResponse("<h1>Welcome {}!</h1>".format(user))
    """
