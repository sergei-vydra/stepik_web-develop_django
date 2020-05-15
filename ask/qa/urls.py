from django.urls import path, re_path
from .views import test, show_page, show_popular, show_question

urlpatterns = [
    path(r'', show_page),
    path(r'login/', test),
    path(r'signup/', test),
    re_path(r'^question/(\d+)/$', show_question),
    path(r'ask/', test),
    path(r'popular/', show_popular),
    path(r'new/', test),
]
