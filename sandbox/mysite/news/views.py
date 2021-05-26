#from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm

# Create your views here.

#def index(request):
#    news = News.objects.all()
#    context = {'news': news, 'title': 'news list',}
#    return render(request, "news/index.html", context)


class HomeNews(ListView):
    model = News
    template_name = "news/home_news_list.html"  # redefine standard template news_list.html
    context_object_name = 'news'
    #queryset = News.objects.filter(is_published=True).select_related('category')
    #extra_context = {'title': 'news list',}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'news list'
        return context

    def get_queryset(self):                           # prefetch_related() - many to many
        return News.objects.filter(is_published=True).select_related('category') # select_related() - foreign key


#def get_category(request, category_id):
#    news = News.objects.filter(category_id=category_id, is_published=True)
#    category = Category.objects.get(pk=category_id)
#    return render(request, 'news/category.html', {'news':news, 'category': category})


class NewsByCategory(ListView):
    model = News
    template_name = "news/home_news_list.html"  # redefine standard template news_list.html
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


#def view_news(request, news_id: int):
#    #news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)
#    return render(request, 'news/view_news.html', {'news_item': news_item})


class ViewNews(DetailView):
    model = News
    #context_object_name = 'news_item'  # as object in template
    #pk_url_kwarg = 'news_id'
    #template_name = "news/news_detail.html"


#def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
#            #news = News.objects.create(**form.cleaned_data)    # for no binding models
#            news = form.save()
#            return redirect(news)
#    else:
#        form = NewsForm()
#    return render(request, 'news/add_news.html', {'form': form})


class CreateNews(CreateView):
    #model = News
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')