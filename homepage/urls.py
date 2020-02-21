from django.urls import path
from profile_app.views import *

from .views import *

app_name = 'homepage'


urlpatterns = [
    path('', get_homepage),
    path('accounts/login/', MainLogin.as_view(), name='login'),
]
