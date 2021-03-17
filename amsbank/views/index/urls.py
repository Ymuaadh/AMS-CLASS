from django.urls import path
from amsbank.views.index import view

urlpatterns = [
    path('index/', view.index_view, name='index'),

]