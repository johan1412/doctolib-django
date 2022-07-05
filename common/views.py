from django.shortcuts import render

# Create your views here.


def common(request):
    return render(request, "index/index.html")