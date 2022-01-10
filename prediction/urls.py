from django.urls import path

from . import views

app_name = 'prediction'

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:sourceID>/<int:companyID>/<int:optionsID>/', views.Display, name='display'),
    path('pickSource', views.pickSource, name ='pickSource'),
    path('<int:sourceID>/pickCompany', views.pickCompany, name ='pickCompany'),
    path('<int:sourceID>/<int:companyID>/pickOptions', views.pickOptions, name ='pickOptions')
]
