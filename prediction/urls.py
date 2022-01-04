from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:companyID>/<int:optionsID>/', views.Display, name='display'),
]
