from django.shortcuts import render

# Create your views here.


def conditions(request):
    d={'a':44,'b':22}
    return render(request,'conditions.html')