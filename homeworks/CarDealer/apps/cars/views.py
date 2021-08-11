from django.shortcuts import get_object_or_404, reverse
from django.views.generic import DetailView, ListView
from django.core import serializers
from django.http import HttpResponse
from .models import *


class CarView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'all_cars_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all().values()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = get_object_or_404(Car, id=self.kwargs['pk'])
        context['single_car'] = Car.objects.filter(id=car.id)
        return context


def serializer_cars(request):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(request.method + '<br>' + data)
