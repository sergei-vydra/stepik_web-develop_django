from django.urls import path, re_path
from .views import test

urlpatterns = [
    path(r'', test),
    path(r'login/', test),
    path(r'signup/', test),
    re_path(r'^question/(\d+)/$', test),
    path(r'ask/', test),
    path(r'popular/', test),
    path(r'new/', test),
]
