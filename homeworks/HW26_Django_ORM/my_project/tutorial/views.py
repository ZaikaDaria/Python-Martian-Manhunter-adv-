from random import randint, choice
from django.shortcuts import render


def status(request):
    context = {
        # "color": (lambda: "%06x" % randint(0, 0xffffff))(),
        "color": lambda: randint(0, 255),
    }
    return render(request, "tutorial/status.html", context)
