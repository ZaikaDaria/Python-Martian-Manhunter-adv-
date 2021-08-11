from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from apps.orders.models import Order
from django.shortcuts import get_object_or_404, reverse


class OrderView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'all_orders_list'

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


def serializer_order(request):
    data = serializers.serialize('json', Order.objects.all())
    return HttpResponse(request.method + '<br>' + data)