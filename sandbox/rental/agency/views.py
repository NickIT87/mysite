from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Apartment, ApartmentGallery


# Create your views here.
class HomePageView(TemplateView):
    template_name = "agency/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        return context


class ApartmentsView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры."
        return context

    def get_queryset(self):
        return Apartment.objects.all()


class ApartmentsAllSaleView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры, продажа."
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type='Продажа')


class ApartmentsAllRentalView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры, аренда."
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type='Аренда')


class ApartmentsAllExchangeView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры, обмен."
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type='Обмен')


class ApartmentsSaleByRoomsNumber(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3
    #allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['rooms_count'] > 0 and self.kwargs['rooms_count'] <= 3:
            context['title'] = "Квартиры, продажа, комнат: " + str(self.kwargs['rooms_count'])
        else:
            context['title'] = "Квартиры, продажа, комнат: 4+"
        return context

    def get_queryset(self):
        if self.kwargs['rooms_count'] > 0 and self.kwargs['rooms_count'] <= 3:
            return Apartment.objects.filter(proposal_type='Продажа', number_of_rooms=self.kwargs['rooms_count'])
        elif self.kwargs['rooms_count'] == 4:
            return Apartment.objects.filter(proposal_type='Продажа', number_of_rooms__gt=3)
        else:
            raise Http404
