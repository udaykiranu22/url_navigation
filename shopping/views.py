from django.shortcuts import render

# Create your views here.


def dress(request):
    return render(request, 'shopping.html')