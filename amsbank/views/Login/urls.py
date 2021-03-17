from django.urls import path
from amsbank.views.Login import login_view

urlpatterns = [
    path('login', login_view.login_post, name='login'),
    path('', login_view.log_out, name='logout')
]