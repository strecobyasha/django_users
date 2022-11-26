from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('secret/', views.secret_page, name='secret_page'),
]
