from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.choice_model, name='choice_model'),
    path('models/<str:model_name>/', views.testing, name='testing')
]