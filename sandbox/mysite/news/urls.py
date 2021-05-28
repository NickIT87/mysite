from django.urls import path

from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('test/', test, name='test'),
    #path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    #path('cat/<int:category_id>', get_category, name='category'),
    path('cat/<int:category_id>', NewsByCategory.as_view(
        #extra_context={'title':'extracontent'}
    ), name='category'),
    #path('news/<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    #path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]