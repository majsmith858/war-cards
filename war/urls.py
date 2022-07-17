from django.urls import path

from . import views
from war.views import index
urlpatterns = [
    path('', index, name='index'),
    ]