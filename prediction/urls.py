from django.urls import path

from . import views

app_name = 'prediction'

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:companyID>/<int:optionsID>/', views.Display, name='display'),
    path('pickCompany', views.pickCompany, name ='pickCompany'),
    path('<int:companyID>/pickOptions', views.pickOptions, name ='pickOptions')
]
