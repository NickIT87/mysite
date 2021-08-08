from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('apartments/', ApartmentsView.as_view(), name='apartments'),
    path('apartments/sale/', ApartmentsAllSaleView.as_view(), name='apartmentsAllSale'),
    path('apartments/rental/', ApartmentsAllRentalView.as_view(), name='apartmentsAllRental'),
    path('apartments/exchange/', ApartmentsAllExchangeView.as_view(), name='apartmentsAllExchange'),
]