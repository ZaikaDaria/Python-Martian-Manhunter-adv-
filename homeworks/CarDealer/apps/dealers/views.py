from django.views.generic import DetailView, ListView
from django.core import serializers
from django.http import HttpResponse
from .models import *


class DealerView(ListView):
    model = Dealer
    template_name = 'dealer_list.html'
    context_object_name = 'all_dealer_list'
    paginate_by = 5

    def get_queryset(self):
        return Dealer.objects.all()


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'dealer_detail.html'
    context_object_name = 'dealers'


def serializer_dealers(request):
    data = serializers.serialize('json', Dealer.objects.all())
    return HttpResponse(request.method + '<br>' + data)
