from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def mail_sender(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                'elanir358@gmail.com',
                ['Nickolazz@protonmail.com'],
                fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('mail')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Форма не валидна')
    else:
        form = ContactForm()
    return render(request, 'news/mail.html', {'form':form})


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


#def index(request):
#    news = News.objects.all()
#    context = {'news': news, 'title': 'news list',}
#    return render(request, "news/index.html", context)


class HomeNews(MyMixin, ListView):
    model = News
    template_name = "news/home_news_list.html"  # redefine standard template news_list.html
    context_object_name = 'news'
    #queryset = News.objects.filter(is_published=True).select_related('category')
    #extra_context = {'title': 'news list',}
    mixin_prop = 'mixin prop'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('news list')  #context['title'] = 'news list'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):                           # prefetch_related() - many to many
        return News.objects.filter(is_published=True).select_related('category') # select_related() - foreign key


#def get_category(request, category_id):
#    news = News.objects.filter(category_id=category_id, is_published=True)
#    category = Category.objects.get(pk=category_id)
#    return render(request, 'news/category.html', {'news':news, 'category': category})


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = "news/home_news_list.html"  # redefine standard template news_list.html
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
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


class CreateNews(LoginRequiredMixin, CreateView):
    #model = News
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/' #reverse_lazy('home')
    raise_exception = True # raise 403 error if not authenticated