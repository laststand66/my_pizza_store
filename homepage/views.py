from django.shortcuts import render

from .models import Pizza

# Create your views here.
def get_homepage(request):
    return render(request, 'index.html')

def menu_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'homepage/menu.html', context={'pizzas': pizzas})
