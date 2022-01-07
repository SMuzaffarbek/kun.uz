from django.urls import path

from .views import home, category_news, new_detail

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category_news, name='category_new'),
    path('new/<slug:slug>/', new_detail, name='new_detail')
]