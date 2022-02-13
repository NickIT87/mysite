from rest_framework.generics import ListAPIView

from core.models import Currency


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()