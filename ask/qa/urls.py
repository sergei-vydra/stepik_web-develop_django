from django.urls import path
from .views import test

urlpatterns = [
    path(r'', test),
    path(r'login/', test),
    path(r'signup/', test),
    path(r'question/<int:id>/', test),
    path(r'ask/', test),
    path(r'popular/', test),
    path(r'new/', test),
]
