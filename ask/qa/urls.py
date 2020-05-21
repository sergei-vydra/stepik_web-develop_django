from django.urls import path, re_path
from .views import test, show_page, show_popular, answer_form, ask_form, signup_form, login_form

urlpatterns = [
    path(r'', show_page),
    path(r'login/', login_form),
    path(r'signup/', signup_form),
    re_path(r'^question/(\d+)/$', answer_form),
    path(r'ask/', ask_form),
    path(r'popular/', show_popular),
    path(r'new/', test),
]
