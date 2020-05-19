from django.urls import path, re_path
from .views import test, show_page, show_popular, answer_form, ask_form

urlpatterns = [
    path(r'', show_page),
    path(r'login/', test),
    path(r'signup/', test),
    re_path(r'^question/(\d+)/$', answer_form),
    path(r'ask/', ask_form),
    path(r'popular/', show_popular),
    path(r'new/', test),
]
