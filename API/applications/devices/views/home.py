from django.shortcuts import render


def homeEndpoint(request):
    return render(request, "home.html")
