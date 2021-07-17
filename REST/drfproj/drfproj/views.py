from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class TesView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'no_of_years_active': 10
        }
        return Response(data)


