from django.urls import path
import include
from . import views


urlpatterns = [

    path('\get_bills', views.index, name='index'),

]

