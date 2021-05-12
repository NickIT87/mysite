from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# Create your views here.
def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'news list'
    }
    return render(request, "news/index.html", context)
