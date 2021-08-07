from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры"
        return context

    def get_queryset(self):
        return Apartment.objects.all()


class ApartmentsAllSaleView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры продажа"
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type='Продажа')


class ApartmentsAllRentalView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры аренда"
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type='Аренда')