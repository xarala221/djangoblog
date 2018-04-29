from django.contrib import admin
from django.conf.urls import url
from account.views import *

app_name = 'account'


urlpatterns = [
    url(r"^login/$", user_login, name="login"),
    url(r"^success/$", login_success, name="success"),
    url(r"^logout/$", user_logout, name="logout"),
]