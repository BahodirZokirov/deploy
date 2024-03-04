from django.shortcuts import render
from .models import Laptop
from django.views.generic import TemplateView, DetailView, ListView
# Create your views here.

class LaptopView(TemplateView):
    template_name = 'home.html'

class LaptopDetailView(DetailView):
    model = Laptop
    template_name = 'laptop_detail.html'

class LaptopListView(ListView):
    model = Laptop
    template_name = 'laptop.html'



# def laptop_info(request):
#     laptop = Laptop.objects.all()
#     context = {
#         "laptops": laptop
#     }
#     return render(request, 'laptop_info.html', context)
#
# def laptop_detail(request, pk):
#     laptop = Laptop.objects.get(id=pk)
#     context = {
#         "laptops": laptop
#     }
#     return render(request, 'laptop_detail.html', context=context)